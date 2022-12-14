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
        video_comment=Count('videocomments', distinct=True)
    ).order_by('-created_at')
    search_fields = [
        'post_location'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VideoSerializer
    queryset = Videos.objects.all().order_by('-created_at')
