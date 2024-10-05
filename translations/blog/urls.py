from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:blog_id>/', views.blog, name='blog')
]