from django.contrib import admin
from blog.models import BlogPostModel, NewsBlogModel, AboutModel, ContactModel, CommentModel
from modeltranslation.admin import TranslationAdmin


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date', 'author' )
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title_en', 'author')
    list_filter = ('id',)


class TodoAdminComments(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'body' )
    list_display_links = ('id', 'post')
    search_fields = ('id', 'namr')
    list_filter = ('id',)

admin.site.register(BlogPostModel, TodoAdmin)
admin.site.register(NewsBlogModel, TodoAdmin)
admin.site.register(AboutModel)
admin.site.register(ContactModel)
admin.site.register(CommentModel, TodoAdminComments)


