from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone

from .models import Post, Comment


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.all()


class PostView(generic.DetailView):
    template_name = 'blog/post.html'


class PostsView(generic.TemplateView): #fixme: to do
    model = Post
    template_name = 'blog/posts.html'


class AboutView(generic.TemplateView):
    template_name = 'blog/about.html'


class ContactView(generic.TemplateView):
    template_name = 'blog/contact.html'
