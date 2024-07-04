from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage, get_connection
from helpers.main import generate_code
from . import serializers
from .models import User, PasswordReset
from .validators import validate_phone_number, validate_email
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator


@extend_schema(tags=['Auth'])
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserRegisterSerializer


@extend_schema(tags=['Auth'])
class UserLoginView(ObtainAuthToken):
    pass


@extend_schema(tags=['Auth'])
class UserLogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Вы вышли из аккаунта'})


@extend_schema(tags=['Auth'])
class RepairUserByPhoneNumberView(generics.GenericAPIView):
    serializer_class = serializers.RepairUserByPhoneSerializer

    # queryset = User.objects.all()
    # lookup_field = None

    def post(self, request):
        data = request.data
        phone_number = validate_phone_number(User, data['phone_number'])
        code = generate_code()

        user = User.objects.get(phone_number=phone_number)
        user.verification_code = code
        # send_sms_code(code, phone_number)
        user.save()
        return Response('ok')


@extend_schema(tags=['Auth'])
class RepairUserByEmailView(generics.GenericAPIView):
    serializer_class = serializers.RepairUserByEmailSerializer

    def post(self, request):
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
                # use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            # print(connection)
            EmailMessage(
                'Восстановление пароля',
                f'Ссылка для восстановление пароля: {reset_url}',
                settings.EMAIL_HOST_USER,
                [email],
                connection=connection
            ).send()
        return Response({'status': True, 'reset_token': token})


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = serializers.PasswordResetSerializer
    permission_classes = []

    def post(self, request, token):
        serializer = self.serializer_class(data=request.data)
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
        else:
            return Response({'error': 'No user found'}, status=404)


class CheckVerificationCodeView(generics.GenericAPIView):
    serializer_class = serializers.CodeVerificationSerializer

    def post(self):
        pass

# /<username>/info/edit/
# /<username>/passport/add/

