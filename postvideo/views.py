from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions, generics, filters
from .models import VideoPost
from .serializers import PostVideoSerializer
from skt_drf_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class VideoPostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostVideoSerializer
    queryset = VideoPost.objects.all().order_by('created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile',
        'Post_location'
    ]
    search_fields = [
        'owner__username',
        'title',
        'Post_location'
    ]
    ordering_fields = [
        'comments_count',
        'like_count',
        'likes__created_at'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
