from django import forms
from blog.models import BlogPostModel, NewsBlogModel, AboutModel, ContactModel, CommentModel


class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPostModel
        fields = ['title_en', 'title_ru', 'body_en', 'body_ru', 'image_en', 'image_ru']


class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPostModel
        fields = ['title', 'body', 'image']


class NewsBlogForm(forms.ModelForm):
    class Meta:
        model = NewsBlogModel
        fields = ['title_en', 'title_ru', 'body_en', 'body_ru', 'image_en', 'image_ru']


class UpdateNewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsBlogModel
        fields = ['title', 'body', 'image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['title', 'store_address', 'manufacturer_address', 'phone_number1', 'phone_number2',  'email']


class AboutForm(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = ['body_en', 'body_ru']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['body']