from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PostCreateForm, CommentCreateForm
from .models import Post, Comment


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
    }
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=post,
                author=request.user,
                content=form.cleaned_data['content'],
            )
    context['form'] = CommentCreateForm()
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    context = {}
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                author=request.user
            )
            messages.info(request, 'Post Added')
            return redirect('index')
    else:
        form = PostCreateForm()
    context['form'] = form
    return render(request, 'posts/post_create.html', context)


@login_required
def post_delete(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        if request.user != post.author:
            return redirect('index')
        post.delete()
        messages.warning(request, 'Post Deleted')
        return redirect('index')
