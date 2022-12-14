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
    search_fields = [
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
