from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.response import Response


@extend_schema(tags=['Hotels'])
class HotelList(generics.GenericAPIView):
	def get(self, request):
		return Response('working')