from django.shortcuts import get_object_or_404


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'DELETE', 'PUT'])
def playlist_detail(request, playlist_pk):
    playlist = get_object_or_404(Playlist, pk=playlist_pk)
    
    if request.method == 'GET':
        serializer = PlayListSerializer(playlist)
        movies = playlist.movies.all()
        movie_serializer = MovieSerializer(movies, many=True)
        context = {
            'playlist' : serializer.data,
            'movies' : movie_serializer.data
        }
        return Response(context)
    
    elif request.method == 'DELETE':
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = CreatePlayListSerializer(playlist, data=data)

        if serializer.is_valid(raise_exception=True):
            playlist_serializer = serializer.save()
            origin_movies = playlist.movies.all()
            for origin_movie in origin_movies:
                pp = (origin_movie.pk)
                for _ in playlist_serializer.movies.filter():
                    playlist.movies.remove(pp)
            
            for movie_id in data['movies']:
                movie = Movie.objects.get(pk=movie_id)
                playlist.movies.add(movie)
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def playlist_list_profile(request, user_pk):
    if request.method == 'GET':
        playlists = Playlist.objects.all()
        my_playlist = []
        for playlist in playlists:
            if playlist.user_id==user_pk:
                my_playlist.append(playlist)
        serializer =PlayListSerializer(my_playlist, many=True)
        return Response(serializer.data)