from drf_spectacular.utils import extend_schema
from rest_framework import generics
from . import serializers
from .models import User


# /login
# /registration

@extend_schema(tags=['Users'])
class UserRegistrationView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = serializers.UserRegisterSerializer

# /logout
# /code/send
# /code/check
# /reset/phone
# /reset/email
# /reset/password
