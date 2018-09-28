from django.shortcuts import render
from django.utils import timezone

from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_date')

    context = {
        'posts' : posts,
    }
    return render(request, 'blog/post_list.html', context)