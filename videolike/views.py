from rest_framework import generics, permissions
from skt_drf_api.permissions import IsOwnerOrReadOnly
from .models import VideoLike
from .serializers import VideoLikeSerializer


class VideoLikeList(generics.ListCreateAPIView):
    """
    Display lost of all likes in videos
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VideoLikeSerializer
    queryset = VideoLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VideoLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Detailed list of all liked videos
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = VideoLike.objects.all()
    serializer_class = VideoLikeSerializer
