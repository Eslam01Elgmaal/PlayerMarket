from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Players
# Create your views here.

def players_list(request):
    players = Players.objects.all()

    return render(request, 'players/player_list.html', {'players': players})

    




class PlayersDetailView(DetailView):
    model = Players
    template_name = 'players/player_detail.html'
    context_object_name = 'player'
    

