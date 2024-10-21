from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.validators import UniqueValidator

from helpers.main import generate_code, SMSService
from . import messages
from .models import User, Passport, Tourist, Children, UserTemp


class UserTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTemp
        fields = ['data', 'phone_number', 'verification_code']
        read_only_fields = ['phone_number', 'verification_code']

    def validate(self, data):
        password1 = data['data'].pop('password')
        password2 = data['data'].pop('password2')

        if password1 != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})

        data['data']['password'] = password1

        return data

    def create(self, validated_data):
        data = validated_data['data']

        obj = UserTemp(**validated_data)

        verification_code = generate_code()

        obj.phone_number = data['phone_number']
        obj.verification_code = verification_code

        SMSService.send_message(
            phone_number=data['phone_number'],
            message=messages.SMS_REGISTRATION_MESSAGE.format(code=verification_code)
        )

        obj.save()
        return obj


class UserTempCodeVerificationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()
    verification_code = serializers.CharField(required=False)

    class Meta:
        model = UserTemp
        fields = ['phone_number', 'verification_code']


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        validators=[validate_password],
        required=True,
        write_only=True
    )
    password2 = serializers.CharField(
        required=True,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password', 'password2', 'is_verified']
        read_only_fields = ['is_verified']

    def validate(self, attrs: dict):
        password = attrs.pop('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

        attrs['password'] = password
        return attrs

    def create(self, validated_data: dict):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.first_name = validated_data['username']
        user.set_password(password)
        user.save()
        SMSService.send_message(
            phone_number=user.phone_number,
            message=messages.SMS_REGISTRATION_MESSAGE.format(code=user.verification_code),
        )
        return user


class RepairUserByPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number']


class RepairUserByEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.RegexField(
        write_only=True,
        regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        error_messages={
            'invalid': 'Password must be at least 8 characters long with at least one capital letter and symbol'}
    )
    confirm_password = serializers.CharField(write_only=True, required=True)


class CodeVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['verification_code']


class UserRegistrationCodeVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['verification_code']

    def validate(self, attrs):
        verification_code = attrs.get('verification_code')
        user = User.objects.filter(verification_code=verification_code).first()
        if user is None:
            raise serializers.ValidationError({'code': 'Неверный код', 'is_correct': False})
        user.is_active = True
        user.is_verified = True
        user.save()
        return attrs


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ['id', 'first_name', 'lastname', 'surname', 'birth_date', 'seria', 'issued_by', 'issued_date',
                  'citizen', 'user']


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = ['id', 'user', 'first_name', 'lastname', 'birth_date', 'passport_seria_and_number', 'expiration_date',
                  'gender', 'citizen']


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = [
            'id',
            'user',
            'fullname',
            'gender',
            'birth_date',
            'birth_certificate'
        ]

    def create(self, validated_data):
        user = User.objects.get(pk=self.context['user_pk'])
        validated_data['user'] = user
        obj = Children(**validated_data)
        obj.save()
        return obj


class UserDataSerializer(serializers.ModelSerializer):
    passport_data = serializers.SerializerMethodField(method_name='get_passport_data')
    tourists = TouristSerializer(many=True, source='tourist', required=False)
    children = ChildrenSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'birth_date', 'email', 'phone_number', 'gender', 'passport_data',
                  'tourists', 'children']

    def get_passport_data(self, obj) -> ReturnDict:
        passport = obj.passport_data.first()
        serializer = PassportSerializer(passport, many=False)
        return serializer.data


class UserDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['gender', 'email', 'phone_number']
