from django.shortcuts import render
from rest_framework.response import Response

from . import serializers

from rest_framework import generics, status, permissions, views


class RegistrationView(generics.GenericAPIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=dict(user))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(dict(user_data), status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = serializers.LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
