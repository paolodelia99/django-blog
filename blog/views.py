from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse

from .models import Post, Comment


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.all()


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

