from rest_framework import serializers
from .models import Article, ArticleDecoratedTextItem, ArticleTextItem, ArticleImageItem, ArticleTopParagraphs


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'short_description', 'preview_img', 'slug']


class ArticleDecoratedTextItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleDecoratedTextItem
        fields = ['id', 'text']


class ArticleTextItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTextItem
        fields = ['id', 'text']


class ArticleImageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImageItem
        fields = ['id', 'image', 'descr']


class ArticleTopParagraphsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTopParagraphs
        fields = ['id', 'text']


class ArticleDetailSerializer(serializers.ModelSerializer):
    top_paragraphs = ArticleTopParagraphsSerializer(many=True)
    text_items = ArticleTextItemSerializer(many=True)
    image_items = ArticleImageItemSerializer(many=True)
    decorated_text_items = ArticleDecoratedTextItemSerializer(many=True)
    related_articles = serializers.SerializerMethodField(method_name='get_related_articles')

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'short_description',
            'preview_img',
            'preview_text',
            'slug',
            'quote',
            'top_paragraphs',
            'text_items',
            'image_items',
            'decorated_text_items',
            'published_at',
            'related_articles'
        ]

    def get_related_articles(self, obj):
        articles = Article.objects.all()
        articles = [article for article in articles if article.id != obj.id]
        serializer = ArticleSerializer(articles, many=True)
        return serializer.data
