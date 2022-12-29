from django.db import models
from django.contrib.auth.models import User
from videos.models import Videos


class VideoLike(models.Model):
    """
    Video like model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(
        Videos, on_delete=models.CASCADE, related_name='videoslike')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'video']

    def __str__(self):
        return f'{self.id} {self.video}'
