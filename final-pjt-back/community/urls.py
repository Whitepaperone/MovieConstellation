from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.playlist_list, name='playlist_list'),
    path('<int:playlist_pk>/', views.playlist_detail, name='playlist_detail'),
    # path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    # path('<int:review_pk>/like/', views.like, name='like'),
]
