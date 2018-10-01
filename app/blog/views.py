import re

from django.http import HttpResponse, HttpResponseRedirect
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

    :type request: 
    :param request:
    :return:
    """
    if request.method == 'POST':
        # POST 요청이 왔을 경우
        # 새 글을 작성하고 원하는 페이지로 돌아가게 함
        #return HttpResponse
        # 제목: <제목데이터><br> 내용 내용데이터
        title = request.POST['title']
        text = request.POST['text']

        #objects.create() 메서드를 사용해서
        # 새 Post 객체를 생성하며 DB에 저장
        # title, text는 reqeust.POST에서 가져온 내용
        # author는 request.user
        # 리턴하는 결과는 만들어진 Post객체('post'변수)의 title, text속성을 사용

        post = Post.objects.create(
            author = request.user,
            title = title,
            text = text,
        )
        next_path = '/blog-posts/'
        return HttpResponseRedirect(next_path)


    else:
        return render(request, 'blog/post_create.html')
