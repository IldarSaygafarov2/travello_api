from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('media_content', views.StaticMediaContentView)

urlpatterns = [
    path('newsletter/send/', views.NewsletterView.as_view())
]


urlpatterns += router.urls