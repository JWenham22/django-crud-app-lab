from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)
    founded = models.PositiveIntegerField()
    manager = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    
    def __str__(self):
        return self.name

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateField()
    stadium = models.CharField(max_length=100)
    score_home = models.PositiveIntegerField(null=True, blank=True)
    score_away = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"