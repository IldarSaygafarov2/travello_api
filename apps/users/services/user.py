from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage, get_connection
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from helpers.main import SMSService, generate_code
from .. import messages
from .. import serializers
from ..models import User, PasswordReset
from ..validators import validate_phone_number, validate_email


class AuthService:
    @classmethod
    def repair_by_phone_number(cls, request):
        data = request.data
        phone_number = validate_phone_number(User, data['phone_number'])
        code = generate_code()

        user = User.objects.get(phone_number=phone_number)
        user.verification_code = code
        SMSService.send_message(
            phone_number=phone_number,
            message=messages.SMS_PASSWORD_RESET_MESSAGE.format(code=code),
        )
        user.save()
        return Response({
            'status': True
        })

    @classmethod
    def repair_by_email(cls, request):
        data = request.data
        email = validate_email(User, data['email'])

        user = User.objects.get(email=email)

        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        reset = PasswordReset(email=email, token=token)
        reset.save()

        reset_url = f'http://127.0.0.1:8000/api/v1/users/auth/password/reset/{token}'

        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
        ) as connection:
            EmailMessage(
                'Восстановление пароля',
                f'Ссылка для восстановление пароля: {reset_url}',
                settings.EMAIL_HOST_USER,
                [email],
                connection=connection
            ).send()
        return Response({'status': True, 'reset_token': token})

    @classmethod
    def reset_password(cls, request, token):
        serializer = serializers.PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        new_password = data['new_password']
        confirm_password = data['confirm_password']
        if new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)
        reset_obj = PasswordReset.objects.filter(token=token).first()
        if not reset_obj:
            return Response({'error': 'Invalid token'}, status=400)
        user = User.objects.filter(email=reset_obj.email).first()
        if user:
            user.set_password(request.data['new_password'])
            user.save()
            reset_obj.delete()
            return Response({'success': 'Password updated'})
        return Response({'error': 'No user found'}, status=404)

    @classmethod
    def create_update_passport(cls, request, pk):
        data = request.data
        user = User.objects.get(pk=pk)
        user_passport = user.passport_data.first()
        user_serializer = serializers.UserDataSerializer(user, many=False)
        if user_passport is not None:
            update_passport_serializer = serializers.PassportSerializer(instance=user_passport, data=data)
            update_passport_serializer.is_valid(raise_exception=True)
            update_passport_serializer.save()
            return Response(user_serializer.data)
        serializer = serializers.PassportSerializer(data=data, context={'user_pk': user.pk})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @classmethod
    def check_verification_code(cls, request):
        data = request.data
        user = User.objects.filter(verification_code=data['verification_code']).first()
        if user is None:
            return Response({'is_code_valid': False})
        return Response({'is_code_valid': True})

    @classmethod
    def check_user_registration_verification_code(cls, request):
        verification_code = request.data['verification_code']
        user = User.objects.filter(verification_code=verification_code).first()
        if user is None:
            raise ValidationError({'is_code_valid': False})
        user.is_active = True
        user.is_verified = True
        user.save()
        return Response({'is_code_valid': True})