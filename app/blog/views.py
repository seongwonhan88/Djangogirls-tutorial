from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
import os

def post_list(request):
    # bring template
    template = loader.get_template('blog/post_list.html')
    # template rendering

    context = {}
    content = template.render(context, request)
    return HttpResponse(content)

