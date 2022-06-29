from django.urls import path
from blog.api.views import blog_api, blog_view, blog_detail, blog_create, blog_update, blog_delete
from rest_framework import routers


app_name = 'blog_api'

urlpatterns = [
    path('', blog_api),
    path('blogs', blog_view),
    path('blog_detail/<int:pk>', blog_detail),
    path('blog_create', blog_create),
    path('blog_update/<int:pk>', blog_update),
    path('blog_delete/<int:pk>', blog_delete),
    # path('api/v1/comments', blog_comments),

]
