from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:post_pk>/', views.post_detail, name='post-detail'),
    path('create/', views.post_create, name='create'),
]
