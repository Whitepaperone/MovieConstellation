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
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import SignUpSerializer, ProfileSerializer
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


# 로그인 필요
@api_view(['GET'])
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(person)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


# @require_POST
@api_view(['GET','POST'])
def follow(request, user_pk):
    # pass
    User = get_user_model()
    you = get_object_or_404(User, pk=user_pk)
    me = request.user
    if request.method=='POST':
        if you != me:
            if you.followers.filter(pk=me.pk).exists():
                print('unfollow')
                you.followers.remove(me)
                is_followed = False
            else:
                print('follow')
                you.followers.add(me)
                is_followed = True            
    else:
        if you.followers.filter(pk=me.pk).exists():
                is_followed = True
        else:
            is_followed = False
            
    follower_list=[]
    for i in you.followers.all():
        follower_list.append(i)
    follower=ProfileSerializer(follower_list,many=True)
    
    following_list=[]
    print()
    for i in you.followings.all():
        following_list.append(i)
    following=ProfileSerializer(following_list,many=True)
    context = {
        'followings':following.data,
        'followers':follower.data,
        'is_followed': is_followed,
        'followers_count': you.followers.count(),
        'followings_count': you.followings.count(),
    }
    return Response(context)
