from django.shortcuts import render
from django.utils import timezone

from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    content = ''
    content += '<ul>'

    for post in posts:
        content += f'<li>{post.title}</li>'
    content += '</ul>'

    context = {
        'posts' : content,
    }
    return render(request, 'blog/post_list.html', context)