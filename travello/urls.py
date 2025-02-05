from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from django.conf.urls import i18n

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/auth/', include('apps.users_auth.urls')),
    path('api/v1/articles/', include('apps.articles.urls')),
    path('api/v1/events/', include('apps.events.urls')),
    path('api/v1/main/', include('apps.main.urls')),
    path('api/v1/hotels/', include('apps.hotels.urls')),
    path('api/v1/reviews/', include('apps.reviews.urls')),
    path('api/v1/clients/', include('apps.corporate_clients.urls')),
    path('api/v1/roles/', include('apps.roles.urls')),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('i18n/', include('django.conf.urls.i18n')),
    # path(r'^_nested_admin/', include('nested_admin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
