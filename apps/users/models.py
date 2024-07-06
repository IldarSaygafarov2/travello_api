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


class Passport(models.Model):
	first_name = models.CharField(verbose_name='Имя', max_length=100)
	lastname = models.CharField(verbose_name='Фамилия', max_length=100)
	surname = models.CharField(verbose_name='Отчество', max_length=100)
	birth_date = models.DateField()
	seria = models.CharField(verbose_name='Серия', max_length=100)
	issued_by = models.CharField(verbose_name='Кем выдан', max_length=150)
	issued_date = models.DateField()
	citizen = models.CharField(verbose_name='Гражданство', max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passport_data', verbose_name='Пользователь')

	def __str__(self):
		return f'{self.lastname} {self.first_name} {self.surname}: {self.seria}'

	class Meta:
		verbose_name = 'Паспортные данные'
		verbose_name_plural = 'Паспортные данные'
