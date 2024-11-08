from django_filters.filterset import FilterSet, DateFilter
from apps.events.models import Event


class EventSearchFilter(FilterSet):
    event_start = DateFilter(field_name='event_start', lookup_expr='gte')

    class Meta:
        model = Event
        fields = [
            'country_from',
            'country',
            'event_start',
            'nights',
            'people_in_group'
        ]
