from drf_spectacular.utils import extend_schema
from rest_framework import generics, filters

from .models import Article
from .serializers import ArticleSerializer, ArticleDetailSerializer


@extend_schema(tags=['Articles'])
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


@extend_schema(tags=['Articles'])
class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'


