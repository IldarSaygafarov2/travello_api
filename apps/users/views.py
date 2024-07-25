from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import User, Tourist, Children
from .services.user import AuthService


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

    def post(self, request):
        return AuthService.repair_by_phone_number(request)


@extend_schema(tags=['Auth'])
class RepairUserByEmailView(generics.GenericAPIView):
    serializer_class = serializers.RepairUserByEmailSerializer

    def post(self, request):
        return AuthService.repair_by_email(request)


@extend_schema(tags=['Auth'])
class ResetPasswordView(generics.GenericAPIView):
    serializer_class = serializers.PasswordResetSerializer
    permission_classes = []

    def post(self, request, token):
        AuthService.reset_password(request, token)


@extend_schema(tags=['Auth'])
class CheckVerificationCodeView(generics.GenericAPIView):
    serializer_class = serializers.CodeVerificationSerializer

    def post(self, request):
        return AuthService.check_verification_code(request)


@extend_schema(tags=['Auth'])
class UserRegistrationCheckVerificationCodeView(generics.GenericAPIView):
    serializer_class = serializers.UserRegistrationCodeVerificationSerializer

    def post(self, request):
        pass


@extend_schema(tags=['Users'])
class UserDataView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDataSerializer


@extend_schema(tags=['Users'])
class UserDataUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDataUpdateSerializer


@extend_schema(tags=['Users'])
class UserPassportView(generics.GenericAPIView):
    serializer_class = serializers.PassportSerializer

    def post(self, request, pk):
        return AuthService.create_update_passport(request, pk)


@extend_schema(tags=['Users'])
class TouristCreateView(generics.CreateAPIView):
    """"""
    queryset = Tourist.objects.all()
    serializer_class = serializers.TouristSerializer


@extend_schema(tags=['Users'])
class ChildCreateView(generics.CreateAPIView):
    queryset = Children.objects.all()
    serializer_class = serializers.ChildrenSerializer
