from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, max_length=50)
    password2 = serializers.CharField(write_only=True, min_length=6, max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password', 'password2']

    def validate(self, attrs):
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError(self.default_error_messages)

        password1 = attrs.pop('password')
        password2 = attrs.pop('password2')

        if password1 != password2:
            raise serializers.ValidationError(self.default_error_messages)

        attrs['password'] = password1
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, max_length=50)
    username = serializers.CharField(max_length=255)

    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['password', 'username', 'tokens']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials')
        if not user.is_active:
            raise AuthenticationFailed('User account is disabled')

        return {
            'username': username,
            'tokens': user.tokens
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs.get('refresh')
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('invalid_token')

