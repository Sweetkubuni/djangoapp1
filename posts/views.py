# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
def index(request):
    lastest_posts = Post.objects.order_by('post_date')[:10]
    context = {
        'lastest_posts' : lastest_posts
    }
    return render(request, 'posts/site/index.html', context)

