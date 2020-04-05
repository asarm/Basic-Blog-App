from django.shortcuts import render,get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all().order_by("-created_date")
    
    context = {
        'Post':Post,
        'posts':posts,

    }
    return render(request,'Blog/main.html',context)

def detail(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    context = {
        'Post':post,
    }
    return render(request,'Blog/detail_page.html',context)
