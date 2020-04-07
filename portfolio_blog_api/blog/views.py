from rest_framework import generics
from blog.serializers import PostSerializer
from blog.models import Post

class PostListView(generics.ListAPIView):
    model = Post
    queryset = Post.objects.order_by('-id')
    serializer_class = PostSerializer

class PostListViewThree(generics.ListAPIView):
    model = Post
    posts = Post.objects.all()
    queryset = Post.objects.filter(id__gt = len(posts) - 3).order_by('-id')
    serializer_class = PostSerializer

# class PostListViewPaginated()

class PostDetailView(generics.RetrieveAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
