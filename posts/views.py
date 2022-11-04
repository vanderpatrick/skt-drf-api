from rest_framework import status, permissions, generics, filters
from .models import Post
from .serializers import PostSerializer
from skt_drf_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()