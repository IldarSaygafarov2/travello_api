from django.urls import path
from rest_framework_nested import routers

from apps.tours_booked.views import EventBookingViewSet
from apps.tours_favorites.views import FavoriteTourView
from . import views

router = routers.DefaultRouter()
router.register('', views.UserDataView)

tourists_router = routers.NestedDefaultRouter(router, '', lookup='user')
tourists_router.register('tourists', views.TouristView)

children_router = routers.NestedDefaultRouter(router, '', lookup='user')
children_router.register('children', views.ChildrenView)

passport_router = routers.NestedDefaultRouter(router, '', lookup='user')
passport_router.register('passport', views.UserPassportView)

favorite_tours_router = routers.NestedDefaultRouter(router, '', lookup='user')
favorite_tours_router.register('favorite_tours', FavoriteTourView)

booked_events_router = routers.NestedDefaultRouter(router, '', lookup='user')
booked_events_router.register('booked_events', EventBookingViewSet)

app_name = 'users'

urlpatterns = [
    path('<int:pk>/info/update/', views.UserDataUpdateView.as_view(), name='user-data-update'),
]

urlpatterns += (router.urls +
                tourists_router.urls +
                children_router.urls +
                passport_router.urls +
                favorite_tours_router.urls +
                booked_events_router.urls
                )
