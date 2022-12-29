from rest_framework import generics, permissions
from skt_drf_api.permissions import IsOwnerOrReadOnly
from .models import VideoDislike
from .serializers import VideoDislikeSerializer


class VideoDislikeList(generics.ListCreateAPIView):
    """
    List of all  disliked video posts
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VideoDislikeSerializer
    queryset = VideoDislike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VideoDislikeDetail(generics.RetrieveDestroyAPIView):
    """
    Detailed list of video posts dislikes
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = VideoDislike.objects.all()
    serializer_class = VideoDislikeSerializer
