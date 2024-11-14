from django.urls import path

from .views import (
    UserTourRouteView,
    UserTourCreateView
)

urlpatterns = [
    path('<int:pk>/routes/', UserTourRouteView.as_view(), name='user-routes'),
    path('<int:pk>/routes/create', UserTourCreateView.as_view(), name='user-routes-create'),
]

