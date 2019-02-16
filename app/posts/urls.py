from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('<int:post_pk>/', views.post_detail, name='detail'),
    path('<int:post_pk>/delete/', views.post_delete, name='delete'),
]
