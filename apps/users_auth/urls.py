from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


name = 'users_auth'

urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
