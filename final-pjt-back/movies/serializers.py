from rest_framework import serializers
from .models import Movie,Genre

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields='__all__'


class LikeMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')
        read_only_fields = ('overview','like_users')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name')