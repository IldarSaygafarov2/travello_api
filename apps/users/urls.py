from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'users'

urlpatterns = [
	path('auth/registration/', views.UserRegistrationView.as_view()),
	path('auth/login/', views.UserLoginView.as_view(), name='login'),
	path('auth/logout/', views.UserLogoutView.as_view(), name='logout')
]
