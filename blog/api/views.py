from django.forms import model_to_dict
from django.http import HttpResponse
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from blog.models import BlogPostModel, CommentModel
from blog.api.serializers import BlogSerializer, CreateBlogSerializer, CommentSerializer


@api_view(['GET'])
def blog_api(request):
    api_urls = {
        'Blogs': '/api/v1/blogs/',
        'Detail View': '/api/v1/blog_detail/<str:pk>',
        'Create': '/api/v1/blog_create/',
        'Update': '/task-update/<int:pk>',
        'Delete': '/task-delete/<int:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def blog_view(request):
    user = request.user
    blogs = BlogPostModel.objects.filter(author=user.id).order_by('-id')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPostModel, pk=pk)
    serializer = BlogSerializer(blog_post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def blog_create(request):
    serializer = CreateBlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
    return Response(serializer.data)


@api_view(['POST'])
def blog_update(request, pk):
    user = request.user
    blog_post = get_object_or_404(BlogPostModel, pk=pk)
    if blog_post.author != user:
        return Response({'message': 'You are not the author of that post.'})
    serializer = CreateBlogSerializer(instance=blog_post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def blog_delete(request, pk):
    blog = BlogPostModel.objects.get(id=pk)
    blog.delete()
    return Response('Item successfully delete!')




# @api_view(['GET', 'POST'])
# def blog_comments(request):
#     user = request.user
#     if request.method == 'GET':
#         comment = BlogPostModel.objects.filter(f_name=user.f_name).first()
#         serializer = CommentSerializer(comment, many=True)
#         return Response(serializer.data)



# @api_view(['GET'])
# def blog_comments(request, pk):
#     comments = CommentModel.objects.get(id=pk)
#     comment_serialize = CommentSerializer(comments, many=False)
#     return Response(comment_serialize.data)


# @api_view(['GET'])
# def blog_view(request):
#     blogs = BlogPostModel.objects.all().order_by('-id')
#     serializer = BlogSerializer(blogs, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def blog_detail(request, pk):
#     blog = BlogPostModel.objects.get(id=pk)
#     serializer = BlogSerializer(blog, many=False)
#     return Response(serializer.data)

