from pyexpat.errors import messages
import email
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.forms import BlogPostModel, NewsBlogForm, UpdateBlogPostForm, UpdateNewsPostForm, CreateBlogPostForm, CommentForm
from blog.models import BlogPostModel, NewsBlogModel, AboutModel, ContactModel, CommentModel
from account.models import Account
from django.core.paginator import Paginator
from django.db.models import Q



#BLOGS


@login_required
def blog_view(request):
    context = {}
    user = request.user
    sidebar = Account.objects.filter(id=user.id)
    blogs = BlogPostModel.objects.filter(author=user.id)

    paginator = Paginator(blogs, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['sidebar'] = sidebar
    context['blog'] = blogs
    context['page_obj'] = page_obj

    return render(request, 'blog_posts.html', context)




@login_required
def create_blog(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("account:signin")

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = BlogPostModel()
        return redirect("blog:blog_view")

    sidebar = Account.objects.filter(id=user.id)
    context['form'] = form
    context['sidebar'] = sidebar

    return render(request, "create_blog.html", context)


@login_required
def detail_blog(request, pk):
    context = {}
    user = request.user

    blog_post = get_object_or_404(BlogPostModel, pk=pk)
    sidebar = Account.objects.filter(id=user.id)
    context['sidebar'] = sidebar
    context['blog_detail'] = blog_post

    return render(request, 'blog_detail.html', context)


@login_required
def edit_blog(request, pk):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    blog_post = get_object_or_404(BlogPostModel, pk=pk)

    if blog_post.author != user:
        return HttpResponse('You are not the author of that post.')

    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj
            return redirect('blog:blog_view')
    form = UpdateBlogPostForm(
        initial={
            'title': blog_post.title,
            'body': blog_post.body,
            'image': blog_post.image,
        }
    )
    sidebar = Account.objects.filter(id=user.id)
    context['sidebar'] = sidebar
    context['form'] = form
    return render(request, 'blog_edit.html', context)

@login_required
def delete_blog(request, pk):
    try:
        blog = BlogPostModel.objects.get(id=pk)
    except:
        return HttpResponse("This blog not found!")

    blog.delete()
    return redirect('blog:blog_view')


#NEWS


@login_required
def news_view(request):
    context = {}
    user = request.user

    sidebar = Account.objects.filter(id=user.id)
    blogs = NewsBlogModel.objects.all()

    paginator = Paginator(blogs, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj
    context['sidebar'] = sidebar
    context['news'] = blogs
    return render(request, 'news.html', context)


@login_required
def create_news(request):

    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("account:signin")

    if not user.is_superuser:
        return HttpResponse("Only an admin can create a post!")

    form = NewsBlogForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        # print(obj.author)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        # print(obj.author)
        obj.save()
        form = NewsBlogForm()
        return redirect("blog:news")

    sidebar = Account.objects.filter(id=user.id)
    context['news'] = form
    context['sidebar'] = sidebar

    return render(request, "create_news.html", context)


@login_required
def detail_news(request, pk):
    context = {}
    user = request.user

    news_post = get_object_or_404(NewsBlogModel, pk=pk)
    sidebar = Account.objects.filter(id=user.id)
    context['sidebar'] = sidebar
    context['news_detail'] = news_post

    return render(request, 'news_detail.html', context)


@login_required
def edit_news(request, pk):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('account:signin')

    if not user.is_superuser:
        return HttpResponse("Only an admin can edit a post!")

    blog_news = get_object_or_404(NewsBlogModel, pk=pk)

    if blog_news.author != user:
        return HttpResponse('You are not the author of that post.')

    if request.POST:
        form = UpdateNewsPostForm(request.POST or None, request.FILES or None, instance=blog_news)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj
            return redirect('blog:news')
    form = UpdateNewsPostForm(
        initial={
            'title': blog_news.title,
            'body': blog_news.body,
            'image': blog_news.image,
        }
    )
    sidebar = Account.objects.filter(id=user.id)
    context['sidebar'] = sidebar
    context['form'] = form
    return render(request, 'news_edit.html', context)


@login_required
def delete_news(request, pk):
    user = request.user

    if not user.is_superuser:
        return HttpResponse("Only an admin can delete a post!")

    try:
        news = NewsBlogModel.objects.get(id=pk)
    except:
        return HttpResponse("This blog not found!")

    news.delete()
    return redirect('blog:news')


#OTHER PAGES


@login_required
def contact_view(request):
    context = {}
    user = request.user
    sidebar = Account.objects.filter(id=user.id)
    contact_data = ContactModel.objects.all()
    context['sidebar'] = sidebar
    context['contact_data'] = contact_data
    return render(request, 'contact.html', context)


@login_required
def about_view(request):
    context = {}
    user = request.user
    sidebar = Account.objects.filter(id=user.id)
    about_data = AboutModel.objects.all()
    context['sidebar'] = sidebar
    context['about_data'] = about_data
    return render(request, 'about.html', context)

#POSTS

@login_required
def posts_view(request):
    context = {}
    user = request.user
    sidebar = Account.objects.filter(id=user.id)

    blogs = BlogPostModel.objects.filter(author=user.id)

    posts = BlogPostModel.objects.filter(~Q(author=user))
    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['sidebar'] = sidebar
    context['blog'] = blogs
    context['page_obj'] = page_obj
    context['posts'] = posts
    return render(request, 'posts.html', context)


#COMMENT

@login_required
def blog_comment(request, pk):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("account:signin")

    post = get_object_or_404(BlogPostModel, pk=pk)

    form = CommentForm(request.POST or None, request.FILES or None)

    if form.errors:
        return HttpResponse(form.errors)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.post = post
        obj.save()
        form = CommentModel()
        return redirect("blog:blog_view")

    sidebar = Account.objects.filter(id=user.id)
    context['form'] = form
    context['sidebar'] = sidebar

    return render(request, "add_comment.html", context)


@login_required
def post_comment(request, pk):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("account:signin")

    post = get_object_or_404(BlogPostModel, pk=pk)

    form = CommentForm(request.POST or None, request.FILES or None)
    print(form.errors)
    if form.errors:
        return HttpResponse(form.errors)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.post = post
        obj.save()
        form = CommentModel()
        return redirect("blog:posts")

    sidebar = Account.objects.filter(id=user.id)
    context['form'] = form
    context['sidebar'] = sidebar

    return render(request, "add_comment.html", context)