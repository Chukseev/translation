from django.shortcuts import render
from .models import BlogEntry


def blogs(request):
    blogs = BlogEntry.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context)


def blog(request, blog_id):
    blog = BlogEntry.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/blog.html', context)