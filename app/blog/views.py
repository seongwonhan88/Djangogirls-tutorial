from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.utils import timezone
import os

def post_list(request):
    # bring template
    template = loader.get_template('blog/post_list.html')
    # template rendering

    context = {
        'name': 'seongwon'
    }
    # content = template.render(context, request)
    # return HttpResponse(content)

    return render(request, 'blog/post_list.html', context)