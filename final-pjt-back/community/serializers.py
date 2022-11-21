from rest_framework import serializers
from .models import Playlist

class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
        read_only_fields = ('user', 'like_users')

class CreatePlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
        read_only_fields = ('user', 'like_users', 'movies')