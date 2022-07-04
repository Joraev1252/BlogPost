from rest_framework import serializers
from blog.models import BlogPostModel, CommentModel, NewsBlogModel, AboutModel, ContactModel


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostModel
        fields = "__all__"


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostModel
        fields = ['title_en', 'title_ru', 'body_en', 'body_ru', 'image_en', 'image_ru']


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        fields = '__all__'


#*********************news

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsBlogModel
        fields = "__all__"


class CreateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsBlogModel
        fields = ['title_en', 'title_ru', 'body_en', 'body_ru', 'image_en', 'image_ru']


#*********************other pages

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"
