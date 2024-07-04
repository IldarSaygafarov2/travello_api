from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	"""Custom User model."""
	phone_number = models.CharField(verbose_name='Номер телефона', unique=True, max_length=15, null=True)
	surname = models.CharField(verbose_name='Отчество', max_length=30, null=True)
	birth_date = models.DateField(null=True)
	gender = models.CharField(verbose_name='Пол', max_length=10, null=True)
	verification_code = models.CharField(max_length=6, null=True)
	is_verified = models.BooleanField(default=False)
	

class PasswordReset(models.Model):
	email = models.EmailField()
	token = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
