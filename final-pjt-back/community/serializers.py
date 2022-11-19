from rest_framework import serializers
from .models import Review

class PlayListListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'movie_title')

class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'like_users')