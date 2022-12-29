from django.db import models
from django.contrib.auth.models import User
from videos.models import Videos


class VideoDislike(models.Model):
    """
    Video post Dislike model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(
        Videos, on_delete=models.CASCADE, related_name='videodislike')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'video']

    def __str__(self):
        return f'{self.id} dislikes {self.video}'
