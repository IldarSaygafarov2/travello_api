from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import UserInfoSerializer
from .models import (
    Guide,
    GuideTour,
    GuidePassport, GuideTourExpectation
)
from .serializers import (
    GuideSerializer,
    GuideTourSerializer,
    GuidePassportSerializer,
    GuideTourCreateSerializer
)


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
        passport_data = data.pop('passport_data')

        obj = self.get_object()

        guide_passport, created = GuidePassport.objects.get_or_create(
            guide=obj,
            seria_and_number=passport_data.get('seria_and_number'),
        )

        guide_passport_serializer = GuidePassportSerializer(guide_passport, data=passport_data,
                                                             partial=True)
        guide_passport_serializer.is_valid(raise_exception=True)
        guide_passport_serializer.save()

        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        user_serializer = UserInfoSerializer(user, data=guide_info_data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        guide_serializer = self.serializer_class(obj, data=data)
        guide_serializer.is_valid(raise_exception=True)
        guide_serializer.save()

        result = {
            'info': user_serializer.data,
            'passport_data': guide_passport_serializer.data,
            **guide_serializer.data
        }

        return Response(result)


@extend_schema(tags=['Guides'])
class GuideToursListView(generics.ListAPIView):
    queryset = GuideTour.objects.all()
    serializer_class = GuideTourSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id is None:
            return []
        qs = GuideTour.objects.filter(guide__user_id=user_id)
        return qs


@extend_schema(tags=['Guides'])
class GuideTourCreateView(generics.CreateAPIView):
    queryset = GuideTour.objects.all()
    serializer_class = GuideTourCreateSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user_id = kwargs.get('user_id')

        guide = Guide.objects.get(user_id=user_id)
        data['guide'] = guide.pk

        expectations = data.pop('expectations')

        organizational_details = data.pop('organizational_details')
        schedules = data.pop('schedules')
        photos = data.pop('photos')

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer_data = serializer.data

        for expectation in expectations:
            expectation_obj = GuideTourExpectation.objects.create(
                guide_tour_id=serializer_data['id'],
                **expectation
            )
            expectation_obj.save()



        return Response(serializer_data, status=201)
