from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import User, Tourist, Children, Passport, UserTemp
from .services.user import AuthService
from apps.events.serializers import EventSimpleSerializer
from apps.events.models import Event


@extend_schema(tags=['Auth'])
class UserTempAuth(generics.CreateAPIView):
    serializer_class = serializers.UserTempSerializer
    queryset = UserTemp.objects.all()

    # def create(self, request, *args, **kwargs):


@extend_schema(tags=['Auth'])
class UserTempAuthCodeVerification(generics.CreateAPIView):
    serializer_class = serializers.UserTempCodeVerificationSerializer
    queryset = UserTemp.objects.all()
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.data
        temp_data = get_object_or_404(UserTemp, phone_number=data['phone_number'])
        if temp_data.verification_code == data['verification_code']:
            password = temp_data.data.pop('password')
            user = User(**temp_data.data)
            user.set_password(password)
            user.save()
            return Response({'is_verified': True})
        return Response({'is_verified': False})


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
class UserDataView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserDataSerializer


@extend_schema(tags=['Users Personal Info'])
class UserDataUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDataUpdateSerializer


@extend_schema(tags=['Users Passport Info'])
class UserPassportView(viewsets.ModelViewSet):
    serializer_class = serializers.PassportSerializer
    queryset = Passport.objects.all()

    # def post(self, request, pk):
    #     return AuthService.create_update_passport(request, pk)


@extend_schema(tags=['Users Tourist Info'])
class TouristView(viewsets.ModelViewSet):
    queryset = Tourist.objects.all()
    serializer_class = serializers.TouristSerializer


@extend_schema(tags=['Users Children Info'])
class ChildrenView(viewsets.ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = serializers.ChildrenSerializer
