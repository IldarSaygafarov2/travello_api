from django_filters import FilterSet, AllValuesFilter, NumberFilter
from apps.hotels.models import Hotel


class HotelAirPortDistanceFilter(FilterSet):
    distance_to_airport_from = NumberFilter(lookup_expr='gte', field_name='distance_to_airport')
    distance_to_airport_to = NumberFilter(lookup_expr='lte', field_name='distance_to_airport')
    distance_to_beach_from = NumberFilter(lookup_expr='gte', field_name='distance_to_beach')
    distance_to_beach_to = NumberFilter(lookup_expr='lte', field_name='distance_to_beach')

    class Meta:
        model = Hotel
        fields = ['allocation_type', 'rating', 'beach_type',
                  'beach_line', 'stars', 'has_wifi', 'food_type', 'facility']
