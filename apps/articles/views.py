from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import Article
from .serializers import ArticleSerializer


@extend_schema(tags=['Articles'])
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@extend_schema(tags=['Articles'])
class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
