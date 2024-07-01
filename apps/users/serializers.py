from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from helpers.main import generate_code


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
		fields = ['username', 'email', 'phone_number', 'password', 'password2']
	
	def validate(self, attrs: dict):
		password = attrs.pop('password')
		password2 = attrs.pop('password2')
		
		if password != password2:
			raise serializers.ValidationError({"password": "Пароли не совпадают"})
		
		attrs['password'] = password
		return attrs
	
	def create(self, validated_data: dict):
		password = validated_data.pop('password')
		verification_code = generate_code()
		
		user = User(**validated_data)
		user.first_name = validated_data['username']
		user.set_password(password)
		user.verification_code = verification_code
		
		# нужно отправлять сообщение на номер телефона с кодом подтверждения
		
		user.save()
		return user
		