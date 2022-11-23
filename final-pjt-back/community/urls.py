from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.playlist_list, name='playlist_list'),
    path('<int:playlist_pk>/', views.playlist_detail, name='playlist_detail'),
    path('profileplaylist/<int:user_pk>/', views.playlist_list_profile, name='playlist_list_profile'),
]
