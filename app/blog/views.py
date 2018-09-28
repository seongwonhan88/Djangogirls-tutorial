import re

from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_date')

    context = {
        'posts' : posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post' : post
    }
    # templates/blog/post_detail.html
    # post 가 가진 title, text, author. created_date, pubslished_date 출력
    # return HttpResponse(post.title)
    return render(request, 'blog/post_detail.html', context)