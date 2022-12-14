from rest_framework import status, permissions, generics, filters
from .models import Videos
from .serializers import VideoSerializer
from skt_drf_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class VideoList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VideoSerializer
    queryset = Videos.objects.annotate(
        video_comments=Count('videocomments', distinct=True),
        video_likes=Count('videoslike', distinct=True),
        video_dislike=Count('videodislike', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    search_fields = [
        'owner__username',
        'title',
        'post_location'
    ]
    ordering_fields = [
       'video_likes',
       'video_dislike'
       'video_comments',
       'videoslike__created_at'
       'videodislike__created_at'
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'videoslike__owner__profile',
        'videodislike__owner__profile',
        'owner__profile',
        'post_location'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VideoSerializer
    queryset = Videos.objects.annotate(
        video_comments=Count('videocomments', distinct=True),
        video_likes=Count('videoslike', distinct=True),
        video_dislike=Count('videodislike', distinct=True)
    ).order_by('-created_at')
