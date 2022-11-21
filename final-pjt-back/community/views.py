from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import JsonResponse


# 이쪽이 VUE랑 연동해서 쓸 모듈들
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    )
from movies.models import Movie
from .models import Playlist
from movies.serializers import MovieSerializer
from .serializers import (
    PlayListSerializer,
    CreatePlayListSerializer
)


@api_view(['GET', 'POST'])
def playlist_list(request):
    if request.method == 'GET':
        playlists = Playlist.objects.all()
        my_playlist = []
        for playlist in playlists:
            if playlist.user_id==request.user.id:
                my_playlist.append(playlist)
        serializer =PlayListSerializer(my_playlist, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        print(data)
        serializer = CreatePlayListSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            playlist = serializer.save(user=request.user)
            for movie_id in data['movies']:
                movie = Movie.objects.get(pk=movie_id)
                playlist.movies.add(movie)
                # serializer.save(movies=data['movies'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'DELETE', 'PUT'])
def playlist_detail(request, playlist_pk):
    playlist = get_object_or_404(Playlist, pk=playlist_pk)
    
    if request.method == 'GET':
        serializer = PlayListSerializer(playlist)
        movies = Movie.objects.all()
        print(movies)
        print('################################################')
        print(playlist.movies)
        movies_list = []
        for movie in movies:
            if movie.movies_playlists.playlist_id == playlist_pk:
                movies_list.append(movie)
        print(movies_list)
        
        # temp = .movies_playlists.filter(pk=playlist.pk)
        # print(temp)
        # for movie in playlist.movies_playlists.filter(pk=)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = PlayListSerializer(playlist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# @require_GET
# def detail(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     comments = review.comment_set.all()
#     comment_form = CommentForm()
#     context = {
#         'review': review,
#         'comment_form': comment_form,
#         'comments': comments,
#     }
#     return render(request, 'community/detail.html', context)

# @require_POST
# def create_comment(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.review = review
#         comment.user = request.user
#         comment.save()
#         return redirect('community:detail', review.pk)
#     context = {
#         'comment_form': comment_form,
#         'review': review,
#         'comments': review.comment_set.all(),
#     }
#     return render(request, 'community/detail.html', context)


# @require_POST
# def like(request, review_pk):
#     if request.user.is_authenticated:
#         review = get_object_or_404(Review, pk=review_pk)
#         user = request.user

#         if review.like_users.filter(pk=user.pk).exists():
#             review.like_users.remove(user)
#             is_liked = False
#         else:
#             review.like_users.add(user)
#             is_liked = True
        
#         like_count = review.like_users.count()    
#         context = {
#             'like_count': like_count,
#             'is_liked': is_liked,
#         }
#         return JsonResponse(context)
#     return redirect('accounts:login')
