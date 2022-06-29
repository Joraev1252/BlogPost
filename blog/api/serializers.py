from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from blog.models import BlogPostModel, CommentModel


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostModel
        fields = "__all__"


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostModel
        fields = ['title_en', 'title_ru', 'body_en', 'body_ru']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['body', 'author' ]



