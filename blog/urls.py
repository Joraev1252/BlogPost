from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('marble/', blog_view, name='blog_view'),
    path('add_blog/', create_blog, name='add_blog'),
    path('detail/<int:pk>', detail_blog, name='blog_detail'),
    path('edit_blog/<int:pk>', edit_blog, name='edit_blog'),
    path('delete/<int:pk>/', delete_blog, name='delete_blog'),



    path('add_news/', create_news, name='news_add'),
    path('news/', news_view, name='news'),
    path('news_detail/<int:pk>', detail_news, name='news_detail'),
    path('edit_news/<int:pk>', edit_news, name='edit_news'),
    path('delete_news/<int:pk>/', delete_news, name='delete_news'),


    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('posts/', posts_view, name='posts'),
    path('add_comment_blogs/<int:pk>', blog_comment, name='blog_comment'),
    path('add_comment/<int:pk>', post_comment, name='post_comment'),

]