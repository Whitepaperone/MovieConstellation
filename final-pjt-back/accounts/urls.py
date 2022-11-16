from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.user, name='user'),
    path('signup/', views.signup, name='signup'),
    path('profile/<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
