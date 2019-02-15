from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PostCreateForm
from .models import Post


def post_detail(request, post_pk):
    context = {}
    post = Post.objects.get(pk=post_pk)
    context['post'] = post
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
            return redirect('index')
    else:
        form = PostCreateForm()
    context['form'] = form
    return render(request, 'posts/post_create.html', context)
