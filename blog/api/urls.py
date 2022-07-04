from django.urls import path
from blog.api.views import *


app_name = 'blog_api'

urlpatterns = [
    path('', blog_api),
    path('blogs', blog_view),
    path('blog_detail/<int:pk>', blog_detail),
    path('blog_create', blog_create),
    path('blog_update/<int:pk>', blog_update),
    path('blog_delete/<int:pk>', blog_delete),
    path('create_blog_comment/<int:pk>', create_blog_comment),
    path('blog_comments/<int:pk>', comments_blog_view),

    path('news', news_view),
    path('news_detail/<int:pk>', news_detail),
    path('news_create', news_create),
    path('news_update/<int:pk>', news_update),
    path('news_delete/<int:pk>', news_delete),

    path('posts', post_view),

    path('about', about_view),
    path('contact', contact_view)
]
