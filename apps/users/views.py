from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import User
from .validators import validate_phone_number
from helpers.main import generate_code, send_sms_code
from django.shortcuts import get_object_or_404


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


class CheckVerificationCodeView(generics.GenericAPIView):
	serializer_class = serializers.CodeVerificationSerializer

	def post(self):
		pass


# /code/check
# /repair/phone
# /repair/email
# /reset/password
