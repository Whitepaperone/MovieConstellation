from django.shortcuts import render
from django.views.decorators.http import require_safe
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Genre
from .serializers import MovieSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def movie_list_create(request):
    if request.method=='GET':
        movies=Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)

# @require_safe
# def index(request):
#     movies = Movie.objects.all()
#     context = {
#         "movies": movies,
#     }
#     return render(request, "movies/index.html", context)
    
@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk) 
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

@require_safe
def recommended(request):
    movies = Movie.objects.order_by('vote_average')
    genres = Genre.objects.order_by('name')
    context = {
        "movies": movies,
        "genres": genres,
    }
    return render(request, "movies/recommended.html", context)


def recommendeddata(request):
    genre_pk = int(request.GET.get('genre'))
    year = request.GET.get('year')
       
    if year == '1990년대':
        movies = Movie.objects.filter(release_date__startswith='199')
    elif year == '2000년대':
        movies = Movie.objects.filter(release_date__startswith='200')
    elif year == '2010년대':
        movies = Movie.objects.filter(release_date__startswith='201')
    elif year == '2020년대':
        movies = Movie.objects.filter(release_date__startswith='20')
    else:
        movies = Movie.objects.filter(release_date__startswith='19')
    
    movies_list = []
    for movie in movies:
        for genre in movie.genres.all():
            if genre_pk == genre.pk:
                movies_list.append({
                    'pk': movie.pk,
                    'title': movie.title,
                    'release_date': movie.release_date,
                    'vote_average': movie.vote_average,
                    'poster_path': movie.poster_path,
                })
        
    response = {
        'moviesList': movies_list,
    }
    return JsonResponse(response)