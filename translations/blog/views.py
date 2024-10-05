from django.shortcuts import render
from .models import BlogEntry, BlogImage


def blogs(request):
    blogs = BlogEntry.objects.order_by('created_at')
    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context)


def blog(request, blog_id):
    article = BlogEntry.objects.get(id=blog_id)
    images = BlogImage.objects.filter(blog_entry__in=article)
    context = {'article': article, 'images': images}
    return render(request, 'blog/blog.html', context)