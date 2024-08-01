from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('auth/registration/', views.UserRegistrationView.as_view()),
    path('auth/login/', views.UserLoginView.as_view(), name='login'),
    path('auth/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('auth/repair/phone/', views.RepairUserByPhoneNumberView.as_view(), name='repair_phone'),
    path('auth/repair/email/', views.RepairUserByEmailView.as_view(), name='repair_email'),
    path('auth/password/reset/<str:token>/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('auth/code/check/', views.CheckVerificationCodeView.as_view(), name='code_check'),
    path('<int:pk>/info/', views.UserDataView.as_view(), name='user-data'),
    path('<int:pk>/info/update/', views.UserDataUpdateView.as_view(), name='user-data-update'),
    path('<int:pk>/passport/add/', views.UserPassportView.as_view(), name='user-passport'),
    path('<int:pk>/tourist/add/', views.TouristCreateView.as_view(), name='tourist-create'),
    # path('<int:pk>/tourist/delete/', views.TouristCreateView.as_view(), name='tourist-delete'),
    path('<int:pk>/children/add/', views.ChildCreateView.as_view(), name='child-create'),
    # path('data/<str:username>/passport/add/', )
]
