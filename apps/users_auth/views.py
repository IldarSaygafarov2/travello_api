from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.services.user import AuthService
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserVerificationCodeSerializer,
    ResetPasswordByEmailSerializer, ResetPasswordSerializer
)


@extend_schema(tags=['Authentication'])
class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer


@extend_schema(tags=['Authentication'])
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


@extend_schema(tags=['Authentication'])
class UserVerificationCodeView(APIView):
    serializer_class = UserVerificationCodeSerializer

    def post(self, request):
        return AuthService.check_verification_code(request)


@extend_schema(tags=['Authentication'])
class UserRequestPasswordResetView(GenericAPIView):
    serializer_class = ResetPasswordByEmailSerializer

    def post(self, request):
        return AuthService.repair_by_email(request)


@extend_schema(tags=['Authentication'])
class UserPasswordResetByEmailView(GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, token):
        return AuthService.reset_password(request, token)
