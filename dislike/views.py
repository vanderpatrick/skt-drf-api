from rest_framework import generics, permissions
from skt_drf_api.permissions import IsOwnerOrReadOnly
from .models import Dislike
from .serializers import DislikeSerializer


class DislikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DislikeSerializer
    queryset = Dislike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DislikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer
