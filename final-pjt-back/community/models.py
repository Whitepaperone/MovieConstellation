from django.db import models
from django.conf import settings
from movies.models import Movie

class Playlist(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='community_user')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_playlists')
    movies = models.ManyToManyField(Movie, related_name='movies_playlists')