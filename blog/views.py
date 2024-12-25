from django.shortcuts import render
from blog.models import Post


def counter(pid):
    post=Post.objects.get(id=pid)
    post.counted_view=post.counted_view+1
    post.save()

def blog_home(request):
    posts=Post.objects.filter(status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)


def blog_single (request,pid):
    post=Post.objects.get(id=pid)
    context={'post':post}
    view=counter(pid)

    return render (request,'blog/blog-single.html',context,) 
