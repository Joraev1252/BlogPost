from django.db.models import Q
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from blog.models import BlogPostModel, CommentModel, NewsBlogModel, AboutModel, ContactModel
from blog.api.serializers import BlogSerializer, CreateBlogSerializer, CommentsSerializer, NewsSerializer, CreateNewsSerializer, AboutSerializer, ContactSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def blog_api(request):
    api_urls = {
        'Blogs': 'blogs/',
        'Detail View': 'blog_detail/<str:pk>',
        'Create': 'blog_create',
        'Update': 'blog_update/<int:pk>',
        'Delete': 'blog_delete/<int:pk>',
    }
    return Response(api_urls)


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def blog_view(request):
    user = request.user
    paginator = PageNumberPagination()
    paginator.page_size = 2
    blogs = BlogPostModel.objects.filter(author=user.id).order_by('-id')
    result_page = paginator.paginate_queryset(blogs, request)
    serializer = BlogSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def blog_detail(request, pk):
    user = request.user
    blog_post = get_object_or_404(BlogPostModel, pk=pk)
    if blog_post.author != user:
        return Response({'message': 'You are not the author of that post.'})
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
    return Response('Item successfully deleted!')


#*********************comments


@api_view(['POST'])
def create_blog_comment(request, pk):
    user = request.user
    blog = get_object_or_404(CommentModel, pk = pk)
    comment = CommentModel(author=user)

    serializer = CommentsSerializer(comment, data=request.data)
    if serializer.is_valid():
        # serializer.author = user
        # serializer.blog = blog
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comments_blog_view(request, pk):
    comments = CommentModel.objects.filter(post_id=pk)
    serializer = CommentsSerializer(comments, many=True)
    return Response(serializer.data)


#*********************news


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def news_view(request):
    user = request.user
    paginator = PageNumberPagination()
    paginator.page_size = 2
    news = NewsBlogModel.objects.all()
    result_page = paginator.paginate_queryset(news, request)
    serializer = NewsSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def news_detail(request, pk):
    user = request.user
    news_post = get_object_or_404(NewsBlogModel, pk=pk)

    serializer = NewsSerializer(news_post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def news_create(request):
    user = request.user

    if not user.is_superuser:
        return Response("Only an admin can create a post!")

    serializer = CreateNewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
    return Response(serializer.data)


@api_view(['POST'])
def news_update(request, pk):
    user = request.user

    if not user.is_superuser:
        return Response("Only an admin can update a post!")

    news_post = get_object_or_404(NewsBlogModel, pk=pk)

    serializer = CreateNewsSerializer(instance=news_post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def news_delete(request, pk):
    user = request.user

    if not user.is_superuser:
        return Response("Only an admin can delete a post!")
    news = NewsBlogModel.objects.get(id=pk)
    news.delete()
    return Response('Item successfully deleted!')


#*********************post


@api_view(['GET', ])
def post_view(request):
    user = request.user
    paginator = PageNumberPagination()
    paginator.page_size = 2

    posts = BlogPostModel.objects.filter(~Q(author=user))

    result_page = paginator.paginate_queryset(posts, request)
    serializer = BlogSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


#*********************other pages


@api_view(['GET', ])
def about_view(request):
    about = AboutModel.objects.all()
    serializer = AboutSerializer(about, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def contact_view(request):
    about = ContactModel.objects.all()
    serializer = ContactSerializer(about, many=True)
    return Response(serializer.data)
