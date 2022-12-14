from rest_framework import serializers
from videos.models import Videos
from videolike.models import VideoLike
from videodislike.models import VideoDislike


class VideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    video_comments = serializers.ReadOnlyField()
    video_likes = serializers.ReadOnlyField()
    video_like_id = serializers.SerializerMethodField()
    video_dislike = serializers.ReadOnlyField()
    video_dislike_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_video_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            videolike = VideoLike.objects.filter(
                owner=user, video=obj
            ).first()
            return videolike.id if videolike else None
        return None

    def get_video_dislike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            video_dislike = VideoDislike.objects.filter(
                owner=user, video=obj
            ).first()
            return video_dislike.id if video_dislike else None
        return None

    class Meta:
        model = Videos
        fields = [
            'video',
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'title', 'content',
            'created_at',
            'updated_at',
            'post_location',
            'video_comments',
            'video_likes',
            'video_dislike',
            'video_like_id',
            'video_dislike_id'
        ]
