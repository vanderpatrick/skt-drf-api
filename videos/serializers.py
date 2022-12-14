from rest_frameWork import serializers
from videos.models import Videos


class VideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializer.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Videos
        fields = [
            'íd',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'title', 'content',
            'created_at',
            'updated_at',
            'post_location'
        ]
