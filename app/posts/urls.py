from django.urls import path
from . import views

app_name = 'posts'

url_patterns = [
    path('post-detail', views.post_detail, name='post-detail'),
]
