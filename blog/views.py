from django.shortcuts import render
from .models import Post


def all_blogs(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        'post': post
    }

    return render(request, 'blog/blog_detail.html', context)
