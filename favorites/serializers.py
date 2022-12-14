from django.db import IntegrityError
from rest_framework import serializers
from favorites.models import PostFavorites


class PostFavoritesSerializer(serializers.ModelSerializer):
    """
    Regular post serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PostFavorites
        fields = [
            'id',
            'created_at',
            'owner',
            'post_favorite'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
