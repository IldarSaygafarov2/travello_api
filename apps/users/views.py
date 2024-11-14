from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework import viewsets

from . import serializers
from .models import User, Tourist, Children, Passport


@extend_schema(tags=['Users'])
class UserDataView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserDataSerializer


@extend_schema(tags=['Users Personal Info'])
class UserDataUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDataUpdateSerializer


@extend_schema(tags=['Users Passport Info'])
class UserPassportView(viewsets.ModelViewSet):
    serializer_class = serializers.PassportSerializer
    queryset = Passport.objects.all()


@extend_schema(tags=['Users Tourist Info'])
class TouristView(viewsets.ModelViewSet):
    queryset = Tourist.objects.all()
    serializer_class = serializers.TouristSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_pk')
        tourists = Tourist.objects.filter(user_id=user_id)
        return tourists


@extend_schema(tags=['Users Children Info'])
class ChildrenView(viewsets.ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = serializers.ChildrenSerializer

    def get_serializer_context(self):
        return {'request': self.request, 'user_pk': self.kwargs['user_pk']}


