from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm
from django.http import JsonResponse

# 이쪽이 VUE랑 연동해서 쓸 모듈들
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import (
    SignUpSerializer,
    ProfileSerializer,
    UserSerializer,
)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)
@api_view(['POST'])
def signup(request):
    # 로그인 된 유저면 목록으로 돌아가게
    # if request.user.is_authenticated:
    #     todos = Todo.objects.all()
    #     todoserializer = TodoSerializer(todos, many=True)
    #     return Response(todoserializer.data)
    
    if request.method == 'POST':
        serializer = SignUpSerializer(data=request.data)
        password = serializer.initial_data.get('password')

        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data.get('password') == serializer.validated_data.get('password_check'):
                user = serializer.save()
                user.set_password(password)
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


def user(request, username):
    User = get_user_model()
    user = User.objects.all(username=username)
    serializer = UserSerializer(user)
    
    return Response(serializer.data)


# 로그인 필요
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(person)
    return Response(serializer.data, status=status.HTTP_200_OK)


# @require_POST
def follow(request, user_pk):
    pass
    # if request.user.is_authenticated:
    #     print(1)
    #     User = get_user_model()
    #     print(2)
    #     print(User)
    #     person = get_object_or_404(User, pk=user_pk)
    #     user = request.user
    #     if person != user:
    #         if person.followers.filter(pk=user.pk).exists():
    #             person.followers.remove(user)
    #             is_followed = False
    #         else:
    #             person.followers.add(user)
    #             is_followed = True
    #         context = {
    #             'is_followed': is_followed,
    #             'followers_count': person.followers.count(),
    #             'followings_count': person.followings.count(),
    #         }
    #         return JsonResponse(context)
    # return redirect('accounts:profile', person.username)
