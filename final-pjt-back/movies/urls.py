from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list_create, name='index'),
    # Example: /blog/search/
    # path('search/<str:search_keyword>/', views.SearchFormView.as_view(), name='search'),
    path('search/', views.search_movie, name='search'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/', views.recommended, name='recommended'),
    path('recommendeddata/',views.recommendeddata, name='recommendeddata'),
]