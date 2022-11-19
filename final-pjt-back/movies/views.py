from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Genre
from .serializers import MovieSerializer

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


class SearchFormView(FormView): 
    form_class = PostSearchForm 
    template_name = 'movies/post_search.html' 
    def form_valid(self, form): 
        searchWord = form.cleaned_data['search_word']
        post_list = Movie.objects.filter(Q(title__icontains=searchWord) | Q(overview__icontains=searchWord) | Q(genres__name__icontains=searchWord)).distinct()
        context = {} 
        context['form'] = form 
        context['search_term'] = searchWord 
        context['object_list'] = post_list 
        
        return  render(self.request, self.template_name, context) # No Redirection



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
        serializer = MovieSerializer(movie, data=request.data)
        print(serializer,movie_pk)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
@api_view(['GET'])
def like(request, user_pk):
#     searchWord=request.GET.get('search')
#     if searchWord:
    movies=Movie.objects.all()
    user_movie_list=[]
    for movie in movies:
        if movie.like_users.filter(pk=user_pk).exists():
            user_movie_list.append({'id': movie.pk,
                'title': movie.title,
                'popularity':movie.popularity,
                'release_date': movie.release_date,
                'vote_count':movie.vote_count,
                'vote_average': movie.vote_average,
                'overview':movie.overview,
                'genres':movie.genres,
                'poster_path': movie.poster_path,})
    print(user_movie_list)
    serializer=MovieSerializer(user_movie_list,many=True)
    print(serializer.data)
    return Response(serializer.data)
    # if request.user.is_authenticated:
    #     review = get_object_or_404(Review, pk=review_pk)
    #     user = request.user

    #     if review.like_users.filter(pk=user.pk).exists():
    #         review.like_users.remove(user)
    #         is_liked = False
    #     else:
    #         review.like_users.add(user)
    #         is_liked = True
        
    #     like_count = review.like_users.count()    
    #     context = {
    #         'like_count': like_count,
    #         'is_liked': is_liked,
    #     }
    #     return JsonResponse(context)
    # return redirect('accounts:login')

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