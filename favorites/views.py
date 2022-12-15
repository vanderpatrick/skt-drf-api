from rest_framework import generics, permissions
from skt_drf_api.permissions import IsOwnerOrReadOnly
from favorites.models import PostFavorites
from favorites.serializers import PostFavoritesSerializer


class PostFavoritesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostFavoritesSerializer
    queryset = PostFavorites.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostFavoritesDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostFavoritesSerializer
    queryset = PostFavorites.objects.all()
