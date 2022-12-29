from rest_framework import generics, permissions
from skt_drf_api.permissions import IsOwnerOrReadOnly
from favorites.models import PostFavorites
from favorites.serializers import PostFavoritesSerializer


class PostFavoritesList(generics.ListCreateAPIView):
    """
    List of all posts that were favorited by an user
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostFavoritesSerializer
    queryset = PostFavorites.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostFavoritesDetail(generics.RetrieveDestroyAPIView):
    """
    Detailed data over the post about the relation
    between user and post
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostFavoritesSerializer
    queryset = PostFavorites.objects.all()
