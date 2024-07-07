from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('auth/registration/', views.UserRegistrationView.as_view()),
    path('auth/login/', views.UserLoginView.as_view(), name='login'),
    path('auth/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('auth/repair/phone/', views.RepairUserByPhoneNumberView.as_view(), name='repair_phone'),
    path('auth/repair/email/', views.RepairUserByEmailView.as_view(), name='repair_email'),
    path('auth/password/reset/<str:token>/', views.ResetPasswordView.as_view()),
    path('<int:pk>/info/', views.UserDataView.as_view(), name='user-data'),
    path('<int:pk>/info/update/', views.UserDataUpdateView.as_view(), name='user-data-update'),
    # path('data/<str:username>/passport/add/', )
]
