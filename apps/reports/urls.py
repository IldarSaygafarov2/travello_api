from django.urls import path
from . import views


app_name = 'reports'

urlpatterns = [
    path('', views.reports_index, name='reports_index'),
    path('logout/', views.user_logout, name='reports_user_logout'),
    path('reports/', views.reports_page, name='reports_page'),
    path('reports/create/daily/', views.create_daily_report, name='create_daily_report'),
    path('reports/download/', views.download_reports, name='download_reports'),
]