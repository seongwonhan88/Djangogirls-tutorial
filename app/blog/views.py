import re

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
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

        # next_path = reverse('post-list')
        # return HttpResponseRedirect(next_path)

        return redirect('post-list')


    else:
        return render(request, 'blog/post_create.html')

def post_update(request, pk):
    # URL
    # /posts/<pk>/update
    # template : blog/post_update.html

    # form 은 post_create.html과 같으나
    # input[name=title]과 textarea[name=text]의 내용을
    # 매개변수의 pK에 해당하는 Post의 title, text 속성으로 미리 채운 상태로 form render
    # context dict에 'post' 키에 해당하는 Post Instance를 담아서 보내 사용


    # post_detail view 에서
    # 특정 pk의 Post를 가져와서 템플릿으로 전달
    # 템플릿에서 전달받은 특정 Post를 사용

    # post_create view에서
    # form 형태 보기
    # input 속성의 기본값은 value
    # textarea 속성의 기본값은 열림/닫힘 태그 사이의 텍스트



    return render(request, 'blog/post_update.html')