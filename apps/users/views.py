from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import User


# /login
# /registration

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

# /logout
# /code/send
# /code/check
# /reset/phone
# /reset/email
# /reset/password
