from django.shortcuts import render
from django.views.generic import DetailView
from .models import Players

# 🔹 API Imports
from rest_framework import generics
from .serializers import PlayerSerializer


def players_list(request):
    players = Players.objects.all()
    return render(request, 'players/player_list.html', {'players': players})






class PlayersDetailView(DetailView):
    model = Players
    template_name = 'players/player_detail.html'
    context_object_name = 'player'



class PlayerListAPI(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer
