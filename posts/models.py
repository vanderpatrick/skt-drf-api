from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
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

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', default='../default_profile_qdjgyp', blank=True
    )
    Post_location = models.CharField(
        max_length=32, choices=Post_location, default="other"
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'