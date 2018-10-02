from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect
from .models import Post

def post_list(request):
    # 1. request.GET 에 페이지 값이 전달이 됨
    # 2. 전체 Post queryset을 사용해서 Paginator에 인스턴스 생성, paginator 변수할당
    # ok
    # 3. paginator 인스턴스의 '.page()' 메소드 호출, 호출 인수에 GET요청에 전달된 'page'값을 사용
    # 4. .page() 메서드 호출 결과를 cur_post_변수에 할당 (page instance)
    # 5. posts 변수를 템플릿으로 전달
    # 6. Page Instance는 순회 가능한 객체이며, 순회시 각 루프마다 해당 Post Instance를 돌려줌
    #     post_list.html에서 해당 객체를 순회하도록 템플릿 구현
    # 7. 템플릿에 '이전', '현재페이지', 다음 링크를 생성

    paginator = Paginator(
        Post.objects.all().order_by('-created_date'),
        5) # show 5 posts per page

    page = request.GET.get('page')

    try:
        #page 변수가 가진 값에 해당하는 Page를 paginator dㅔ서 가져오기 위해 시도
        posts = paginator.page(page)

    except PageNotAnInteger:
        #page가 정수가 아닐 경우 발생하는 예외
        posts = paginator.page(1)
    except EmptyPage:
        # page변수에 해당하는 Page에 내용이 없는 경우 마지막 페이지 가져옴
        posts = paginator.page(paginator.num_pages)

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

    # pk에 대항하는 Post Instance를 'post' 키 값으로 템플릿 렝더링 과정에 전달
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        # form 으로 부터 전달된 데이터를 변수에 할당
        title = request.POST['title']
        text = request.POST['text']
        # 수정할 Post instance의 속성에 전다받은 데이터의 값을 할당

        post.title = title
        post.text = text

        #db에 변경사항 업데이트
        post.save()

        # /post/<pk>/
        #reverse 를 사용해서

        return redirect('post-detail', pk=pk)
    else:
        context = {
            'post' : post,
        }


        return render(request, 'blog/post_update.html', context)