from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from dislike.models import Dislike
from favorites.models import PostFavorites


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    comments_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()
    like_count = serializers.ReadOnlyField()
    post_favorite_id = serializers.SerializerMethodField()
    post_favorite_count = serializers.ReadOnlyField()
    dislike_id = serializers.SerializerMethodField()
    dislike_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_dislike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            dislike = Dislike.objects.filter(
                owner=user, post=obj
            ).first()
            return dislike.id if dislike else None
        return None

    def get_post_favorite_id(self, obj):
        """Method to return saves count for individual user"""
        user = self.context['request'].user
        if user.is_authenticated:
            favorites = PostFavorites.objects.filter(
                owner=user, post_favorite=obj
            ).first()
            return favorites.id if favorites else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'dislike_id', 'dislike_count', 'owner',
            'is_owner', 'post_favorite_id', 'post_favorite_count',
            'profile_id', 'Post_location',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image',
            'like_id', 'comments_count', 'like_count'
        ]
