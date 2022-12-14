from rest_framework import generics, permissions
from skt_drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import VideoComment
from .serializers import VideoCommentSerializer, VideoCommentSerializerDetail


class VideoCommentList(generics.ListCreateAPIView):
    serializer_class = VideoCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    queryset = VideoComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['video']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VideoCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VideoCommentSerializerDetail
    queryset = VideoComment.objects.all()