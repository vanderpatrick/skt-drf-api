from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video

Post_location = [
        ('gap', 'Gap'),
        ('rail', 'Rail'),
        ('ledge', 'Ledge'),
        ('ramps', 'Ramps'),
        ('mini-ramp', 'Mini-Ramp'),
        ('halfpipe', 'Halfpipe'),
        ('street', 'Street'),
        ('park', 'Park'),
        ('other', 'Other'),
    ]


class VideoPost(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    video = models.FileField(
        upload_to='videos/',
        storage=VideoMediaCloudinaryStorage(),
        validators=[validate_video]
    )

    Post_location = models.CharField(
        max_length=50, choices=Post_location,
        default='other'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.id} {self.title}'
