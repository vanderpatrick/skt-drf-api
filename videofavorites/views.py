from rest_framework import generics, permissions
from skt_drf_api.permissions import IsOwnerOrReadOnly
from videofavorites.models import Videofavorites
from videofavorites.serializers import videofavoritesSerializers


class VideofavoritesList(generics.ListCreateAPIView):
    """
    Display list of all favorited video posts
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = videofavoritesSerializers
    queryset = Videofavorites.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VideofavoritesDetail(generics.RetrieveDestroyAPIView):
    """
    Detailed list of favorited video posts
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = videofavoritesSerializers
    queryset = Videofavorites.objects.all()
