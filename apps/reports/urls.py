from django.urls import path
from . import views


app_name = 'reports'

urlpatterns = [
    path('', views.reports_index, name='reports_index'),
    path('reports/', views.reports_page, name='reports_page'),
    path('reports/create/daily/', views.create_daily_report, name='create_daily_report'),
    path('reports/create/agent/', views.create_agent_report, name='create_agent_report'),
    path('reports/create/supplier/', views.create_supplier_report, name='create_supplier_report'),
    path('reports/download/', views.download_reports, name='download_reports'),
]