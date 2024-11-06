from django.urls import path

from .views import (
    UserRegistrationView,
    UserLoginView,
    UserVerificationCodeView,
    UserRequestPasswordResetView,
    UserPasswordResetByEmailView
)

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='auth_register'),
    path('login/', UserLoginView.as_view(), name='auth_login'),
    path('code/check/', UserVerificationCodeView.as_view(), name='auth_code'),
    path('password-reset/request/', UserRequestPasswordResetView.as_view(), name='auth_password_reset'),
    path('password/reset/<str:token>/', UserPasswordResetByEmailView.as_view())
]