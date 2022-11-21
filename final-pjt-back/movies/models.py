from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    # 영화 좋아요
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', null=True)
    
# class Playlist(models.Model):
#     title=models.CharField(max_length=50)
#     movies= models.ManyToManyField(Movie)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    