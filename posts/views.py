from rest_framework import status, permissions, generics, filters
from .models import Post
from .serializers import PostSerializer
from skt_drf_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class PostList(generics.ListCreateAPIView):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        comments_count=Count('comments', distinct=True),
        like_count=Count('likes', distinct=True),
        dislike_count=Count('dislike', distinct=True)
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'dislike__owner__profile',
        'owner__profile',
        'Post_location'
    
    ]
    search_fields = [
        'owner__username',
        'dislike__owner__profile',
        'title',
        'Post_location'
    ]
    ordering_fields = [
        'comments_count',
        'like_count',
        'likes__created_at',
        'dislike__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = queryset = Post.objects.annotate(
        comments_count=Count('comments', distinct=True),
        like_count=Count('likes', distinct=True),
        dislike_count=Count('dislike', distinct=True)
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'comments_count',
        'like_count',
        'likes__created_at'
    ]
