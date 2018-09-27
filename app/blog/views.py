from django.http import HttpResponse
from django.utils import timezone


def post_list(request):
    """

    :param request: 실제 http요청에 대한 정보를 가진 객체
    :return:
    """
    current_time = timezone.now()

    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>Post List</h1>'
        '<p>{}</p>'
        '</body>'
        '</html>'.format(
            # 날짜 시간 객체를 문자열로 변함
            current_time.strftime('%Y. %m. %d<br>%H:%M:%S')
        )
    )
