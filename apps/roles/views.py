from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import UserInfoSerializer
from .models import Guide, GuideTour
from .serializers import GuideSerializer, GuideTourSerializer


@extend_schema(tags=['Guides'])
class GuideDetailView(generics.RetrieveAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    lookup_field = 'user_id'
    lookup_url_kwarg = 'user_id'

    def get_object(self):
        user_id = self.kwargs['user_id']
        guide = get_object_or_404(Guide, user_id=user_id)
        return guide


@extend_schema(tags=['Guides'])
class GuideUpdateView(generics.UpdateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    lookup_field = 'user_id'
    lookup_url_kwarg = 'user_id'

    def update(self, request, *args, **kwargs):
        data = request.data
        guide_info_data = data.pop('info')

        obj = self.get_object()

        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        user_serializer = UserInfoSerializer(user, data=guide_info_data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        guide_serializer = self.serializer_class(obj, data=data)
        guide_serializer.is_valid(raise_exception=True)
        guide_serializer.save()

        return Response(guide_serializer.data)


@extend_schema(tags=['Guides'])
class GuideToursListView(generics.ListAPIView):
    queryset = GuideTour.objects.all()
    serializer_class = GuideTourSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        qs = GuideTour.objects.filter(guide__user_id=user_id)
        return qs
