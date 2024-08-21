from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from . import serializers, models


# Create your views here.
@extend_schema(tags=['Tour Favorites'])
class FavoriteTourView(viewsets.ModelViewSet):
    serializer_class = serializers.TourFavoriteSerializer
    queryset = models.FavoriteTour.objects.all()
    # lookup_url_kwarg = 'user_id'

    def get_serializer_context(self):
        return {'user_id': self.kwargs['user_pk']}
