from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Genre
from .serializers import MovieSerializer,LikeMovieSerializer
import json

from django.views.generic import FormView
from .forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.

@api_view(['GET', 'POST'])
def movie_list_create(request):
    if request.method=='GET':
        movies=Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)

def search_movie(request):
    searchWord=request.GET.get('search')
    if searchWord:
        post_list = Movie.objects.filter(
            Q(title__icontains=searchWord) | Q(overview__icontains=searchWord) | Q(genres__name__icontains=searchWord)
            ).distinct()
        serializer=MovieSerializer(post_list,many=True)
        movie_list=[]
        for movie in post_list:
            movie_list.append({
                'id': movie.pk,
                'title': movie.title,
                'popularity':movie.popularity,
                'release_date': movie.release_date,
                'vote_count':movie.vote_count,
                'vote_average': movie.vote_average,
                'overview':movie.overview,
                'genres':movie.genres,
                'poster_path': movie.poster_path,
            })
        serializer = MovieSerializer(movie_list,many=True)
        response = {
        'movies': serializer.data,
    }
    return JsonResponse(response)


# class SearchFormView(FormView): 
#     form_class = PostSearchForm 
#     template_name = 'movies/post_search.html' 
#     def form_valid(self, form): 
#         searchWord = form.cleaned_data['search_word']
#         post_list = Movie.objects.filter(Q(title__icontains=searchWord) | Q(overview__icontains=searchWord) | Q(genres__name__icontains=searchWord)).distinct()
#         context = {} 
#         context['form'] = form 
#         context['search_term'] = searchWord 
#         context['object_list'] = post_list 
        
#         return  render(self.request, self.template_name, context) # No Redirection



# @require_safe
# def index(request):
#     movies = Movie.objects.all()
#     context = {
#         "movies": movies,
#     }
#     return render(request, "movies/index.html", context)
    
# @require_safe
# def detail(request, movie_pk):
#     movie = Movie.objects.get(pk=movie_pk) 
#     context = {
#         'movie': movie,
#     }
#     return render(request, 'movies/detail.html', context)


@api_view(['GET', 'POST'])
def detail(request,movie_pk):
    
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method=='GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['PUT'])
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'PUT':
        serializer = LikeMovieSerializer(movie,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(like_users=request.data['like_users'])
            return Response(serializer.data)



def like_movie(user_pk):
    movies=Movie.objects.all()
    user_movie_list=[]
    for movie in movies:
        if movie.like_users.filter(pk=user_pk).exists():
            user_movie_list.append(
                {'id': movie.pk,
                'title': movie.title,
                'popularity':movie.popularity,
                'release_date': movie.release_date,
                'vote_count':movie.vote_count,
                'vote_average': movie.vote_average,
                'overview':movie.overview,
                'genres':movie.genres,
                'poster_path': movie.poster_path,})
    return user_movie_list

@api_view(['GET'])
def like(request, user_pk):
    user_movie_list=like_movie(user_pk)
    serializer = MovieSerializer(user_movie_list,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recommend_with_genre(request, user_pk):
    like_movies=like_movie(user_pk)
    like_movies_id=[]
    movies=Movie.objects.all()
    genres=Genre.objects.all()
    like_genres=set()
    for i in like_movies:
        like_movies_id.append(i['id'])
        for g in i['genres'].all():
            like_genres.add(g)
    res=[movie for movie in  movies if movie.id not in like_movies_id]
    recommend={}
    for j in res:
        recommend[j.id]=0
        for g in j.genres.all():
            for genre in like_genres:
                if g==genre:
                    recommend[j.id]+=1
    recommend_list=sorted(recommend.items(), key=lambda item: item[1],reverse=True)
    recommend_movie=[]
    for k,v in recommend_list:
        recommend_movie.append(get_object_or_404(Movie, pk=k))
    serializer=MovieSerializer(recommend_movie,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def combinatnion(request, user_pk,another_user_pk):
    a_like_movies=like_movie(user_pk)
    b_like_movies=like_movie(another_user_pk)

    intersection=[]
    a_complement=a_like_movies[:]
    b_complement=b_like_movies[:]

    for i in a_like_movies:
        for j in b_like_movies:
            if i['id']==j['id']: 
                intersection.append(i)

    for i in a_like_movies:
        for j in intersection:
            if i['id']==j['id']:
                a_complement.remove(i)

    for i in b_like_movies:
        for j in intersection:
            if i['id']==j['id']:
                b_complement.remove(i)
                
    intersection_serializer=MovieSerializer(intersection,many=True)
    a_complement_serializer=MovieSerializer(a_complement,many=True)
    b_complement_serializer=MovieSerializer(b_complement,many=True)

    context={
        'intersection': intersection_serializer.data,
        'a_complement':a_complement_serializer.data,
        'b_complement':b_complement_serializer.data
    }
    return JsonResponse(context)
    pass

# @require_safe
# def recommended(request):
#     movies = Movie.objects.order_by('vote_average')
#     genres = Genre.objects.order_by('name')
#     context = {
#         "movies": movies,
#         "genres": genres,
#     }
#     return render(request, "movies/recommended.html", context)


# def recommendeddata(request):
#     genre_pk = int(request.GET.get('genre'))
#     year = request.GET.get('year')
       
#     if year == '1990년대':
#         movies = Movie.objects.filter(release_date__startswith='199')
#     elif year == '2000년대':
#         movies = Movie.objects.filter(release_date__startswith='200')
#     elif year == '2010년대':
#         movies = Movie.objects.filter(release_date__startswith='201')
#     elif year == '2020년대':
#         movies = Movie.objects.filter(release_date__startswith='20')
#     else:
#         movies = Movie.objects.filter(release_date__startswith='19')
    
#     movies_list = []
#     for movie in movies:
#         for genre in movie.genres.all():
#             if genre_pk == genre.pk:
#                 movies_list.append({
#                     'pk': movie.pk,
#                     'title': movie.title,
#                     'release_date': movie.release_date,
#                     'vote_average': movie.vote_average,
#                     'poster_path': movie.poster_path,
#                 })
        
#     response = {
#         'moviesList': movies_list,
#     }
#     return JsonResponse(response)