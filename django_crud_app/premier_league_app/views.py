from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Team, Player, Match
from django.urls import reverse_lazy

class TeamList(ListView):
    model = Team
    template_name = 'team_list.html'

class TeamDetail(DetailView):
    model = Team
    template_name = 'team_detail.html'

class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = ['name', 'city', 'stadium', 'founded', 'manager']
    success_url = reverse_lazy('team_list')

class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    fields = ['name', 'city', 'stadium', 'founded', 'manager']
    success_url = reverse_lazy('team_list')

class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    success_url = reverse_lazy('team_list')

class PlayerList(ListView):
    model = Player
    template_name = 'player_list.html'

class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['name', 'position', 'age', 'team']
    success_url = reverse_lazy('player_list')

class MatchList(ListView):
    model = Match
    template_name = 'match_list.html'