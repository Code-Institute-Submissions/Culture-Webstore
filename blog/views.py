from django.shortcuts import render
from .models import Post


def all_blogs(request):
    """ A view to render blog posts page """

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, slug):
    """ A view to render blog detail page """

    post = Post.objects.get(slug=slug)

    context = {
        'post': post
    }

    return render(request, 'blog/blog_detail.html', context)
