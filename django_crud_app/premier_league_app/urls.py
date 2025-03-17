from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.TeamList.as_view(), name='team_list'),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name='team_detail'),
    path('teams/create/', views.TeamCreate.as_view(), name='team_create'),
    path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='team_update'),
    path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='team_delete'),
    path('players/', views.PlayerList.as_view(), name='player_list'),
    path('players/create/', views.PlayerCreate.as_view(), name='player_create'),
    path('matches/', views.MatchList.as_view(), name='match_list'),
]