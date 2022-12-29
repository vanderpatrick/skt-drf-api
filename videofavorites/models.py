from django.db import models
from django.contrib.auth.models import User
from videos.models import Videos


class Videofavorites(models.Model):
    """
    Video post favorites model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    videos_favorites = models.ForeignKey(
        Videos, related_name='favorites_videos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'videos_favorites']

    def __str__(self):
        return f'{self.owner} {self.videos_favorites}'
