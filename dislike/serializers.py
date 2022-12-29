from rest_framework import serializers
from django.db import IntegrityError
from .models import Dislike


class DislikeSerializer(serializers.ModelSerializer):
    """
    Dislike serializer
    """
    owner = serializers.ReadOnlyField(source="owner.usernmae")

    class Meta:
        model = Dislike

        fields = ['owner', 'post', 'created_at', 'id']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "possible duplicate"
                })
