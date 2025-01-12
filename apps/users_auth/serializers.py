from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.users.messages import SMS_REGISTRATION_MESSAGE
from apps.users.models import User
from helpers.main import generate_code, SMSService


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "password1", "password2"]

    def validate(self, data):
        password1 = data.pop("password1")
        password2 = data.pop("password2")

        if password1 != password2:
            raise serializers.ValidationError({"detail": "passwords do not match"})

        data["password"] = password2
        return data

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        verification_code = generate_code()
        user.verification_code = verification_code
        SMSService.send_message(
            phone_number=user.phone_number,
            message=SMS_REGISTRATION_MESSAGE.format(code=verification_code),
        )
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    user_type = serializers.CharField(read_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if username is None:
            raise serializers.ValidationError({"detail": "Username is required"})

        if password is None:
            raise serializers.ValidationError({"detail": "Password is required"})

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                {"detail": "Username or Password is invalid"}
            )

        if not user.is_active:
            raise serializers.ValidationError({"detail": "User account is disabled"})

        # if not user.is_verified:
        #     raise serializers.ValidationError(
        #         {"detail": "User account is not verified"}
        #     )

        return {
            "user_id": user.id,
            "username": user.username,
            "user_type": user.user_type,
            "token": user.token,
        }


class UserVerificationCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(write_only=True)
    verification_code = serializers.IntegerField(write_only=True)


class ResetPasswordByEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        write_only=True,
    )
    confirm_password = serializers.CharField(write_only=True, required=True)
