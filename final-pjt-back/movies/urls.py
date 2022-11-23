from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list_create, name='index'),
    path('search/', views.search_movie, name='search'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:user_pk>/like/', views.like, name='like'),
    path('<int:user_pk>/recommend/', views.recommend_with_genre, name='recommend'),
    path('<int:user_pk>/combination/<int:another_user_pk>/',views.combinatnion, name='combination'),
]