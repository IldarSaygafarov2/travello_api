from drf_spectacular.utils import extend_schema
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Article
from .serializers import ArticleSerializer, ArticleDetailSerializer


@extend_schema(tags=['Articles'])
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)
    filterset_fields = ('show_on_home_page',)


@extend_schema(tags=['Articles'])
class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'


