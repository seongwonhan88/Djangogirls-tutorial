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
    return render(request, 'blog/post_detail.html', context)

def post_create(request):
    """
    template : blog/post_create.html 사용
    URL : /posts/create/

    1. 템플릿에 하나의 <form> 요소를 구현
        input[name='title']
        textarea[name = 'text']
        button[type = 'submit']

    2. post_create.html을 보여주는 링크를 base.html에 구현
         {% url %} 태그 사용

    :param request:
    :return:
    """


    return render(request, 'blog/post_create.html')
