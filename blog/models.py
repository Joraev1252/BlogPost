from uuid import uuid4
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from account.models import Account


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = "news_archive/{filename}".format(
        filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class BlogPostModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    publish_date = models.DateField(auto_now_add=True, null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("account:home_page", args=[str(self.id)])


class NewsBlogModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    publish_date = models.DateField(auto_now_add=True, null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("account:home_page", args=[str(self.id)])


class ContactModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    store_address = models.TextField(blank=True, null=True)
    manufacturer_address = models.TextField(blank=True, null=True)
    phone_number1 = models.IntegerField(blank=True, null=True)
    phone_number2 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return str(self.title)


class AboutModel(models.Model):
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.body)


class CommentModel(models.Model):
    post = models.ForeignKey(BlogPostModel, related_name='comments', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title}-{self.author.email}"

    # def get_absolute_url(self):
    #     return reverse("account:home_page", args=[str(self.id)])


