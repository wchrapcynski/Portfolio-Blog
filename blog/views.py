from rest_framework import generics
from blog.serializers import PostSerializer
from blog.models import Post

class PostListView(generics.ListAPIView):
    model = Post
    queryset = Post.objects.order_by('-id')
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
