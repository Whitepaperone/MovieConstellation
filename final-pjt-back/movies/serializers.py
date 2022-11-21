from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields='__all__'


class LikeMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')
        read_only_fields = ('overview','like_users')