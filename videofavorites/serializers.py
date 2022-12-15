from django.db import IntegrityError
from rest_framework import serializers
from videofavorites.models import Videofavorites


class videofavoritesSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Videofavorites
        fields = [
            'id',
            'created_at',
            'owner',
            'videos_favorites'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
