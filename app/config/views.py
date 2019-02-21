from django.shortcuts import render
from posts.models import Post
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    # Reason for declaring <page_num>
    # - To convert DataType str to int
    #   request.GET.page in the template returns str. So it can't use on comparison
    # - To prevent error when page is None
    page_num = page or 1
    context = {
        'posts': paginator.get_page(page),
        'page_num': int(page_num),  # Convert DataType str to int
    }
    return render(request, 'index.html', context)
