from django.shortcuts import render
from posts.models import Post


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)
