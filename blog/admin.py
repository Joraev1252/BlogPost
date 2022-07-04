from django.contrib import admin
from blog.models import BlogPostModel, NewsBlogModel, AboutModel, ContactModel, CommentModel
from modeltranslation.admin import TranslationAdmin


class TodoAdminBlog(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publish_date' )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id', 'author__email')
    list_filter = ('id',)


class TodoAdminComments(admin.ModelAdmin):
    list_display = ('id', 'post', 'body', 'author', 'post_id')
    list_display_links = ('id', 'post')
    search_fields = ('id', 'post')
    list_filter = ('id',)


admin.site.register(BlogPostModel, TodoAdminBlog)
admin.site.register(NewsBlogModel, TodoAdminBlog)
admin.site.register(AboutModel)
admin.site.register(ContactModel)
admin.site.register(CommentModel, TodoAdminComments)

