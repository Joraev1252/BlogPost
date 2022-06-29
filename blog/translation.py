from modeltranslation.translator import register, TranslationOptions
from blog.models import BlogPostModel, NewsBlogModel, AboutModel, ContactModel


@register(BlogPostModel)
class BlogTranslationOptions(TranslationOptions):
    fields = ['title', 'body', 'image']


@register(NewsBlogModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ['title', 'body', 'image']


@register(AboutModel)
class AboutTranslationOptions(TranslationOptions):
    fields = ['body']


@register(ContactModel)
class ContactTranslationOptions(TranslationOptions):
    fields = ['title', 'store_address', 'manufacturer_address']

