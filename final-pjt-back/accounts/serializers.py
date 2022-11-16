from rest_framework import serializers
from django.contrib.auth import get_user_model

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # 회원가입시 입력할 정보
        fields = ('username',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # 프로필시 입력할 정보
        fields = ('username', 'followings',)

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # 프로필시 입력할 정보
        fields = ('username', 'followings',)
