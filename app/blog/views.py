from django.http import HttpResponse
from django.utils import timezone
import os

def post_list(request):
    """

    :param request: 실제 http요청에 대한 정보를 가진 객체
    :return:
    """
    current_time = timezone.now()

    #templates/blog/post_lists.html 파일의 내용을 읽어온 후,
    #해당 내용을 아래에서 리턴해주는 HttpResponse 인스턴스 생성 시 인수로 넣어준다
    # os.path.abspath(__file__) 코드가 실행중인 파일의 경로 표시
    # os.path.dirname(<경로>) 특정경로의 상위 폴더로 이동
    # os.path.join(경로, 폴더/파일명) 특정경로에서 하위폴더 또는 하위 파일을 나타냄

    pwd = os.path.abspath(__file__)
    blog_dir = os.path.dirname(pwd)
    app_dir =  os.path.dirname(blog_dir)
    templates_dir = os.path.join(app_dir, 'templates')
    templates_blog_dir = os.path.join(templates_dir, 'blog')
    post_list_html = os.path.join(templates_blog_dir, 'post_list.html')

    with open(post_list_html, 'rt') as f:
        content = f.read()

    # content = open(post_list_html, 'rt').read()
    return HttpResponse(content)

