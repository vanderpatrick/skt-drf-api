from django.db import models
from django.contrib.auth.models import User
from videos.models import Videos
# Create your models here.


class VideoComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(
        Videos, on_delete=models.CASCADE, related_name='videocomments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

