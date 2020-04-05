from django.shortcuts import (render, get_object_or_404, redirect)
from django.url import reverse_lazy
from django.utils import timezone
from blog.models import Post, Comment
from django.views.generic import(TemplateView, ListView, DetailView)

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Posts.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
