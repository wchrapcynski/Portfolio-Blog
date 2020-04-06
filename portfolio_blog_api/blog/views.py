from rest_framework import permissions, generics
from django.shortcuts import render
from django.utils import timezone
from blog.serializers import PostSerializer
from blog.models import Post

class PostListView(generics.ListAPIView):
    model = Post
    queryset = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
