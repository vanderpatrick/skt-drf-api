from rest_framework import serializers
from django.db import IntegrityError
from .models import VideoDislike


class VideoDislikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = VideoDislike
        fields = [
            'owner', 'video', 'created_at', 'id'
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
