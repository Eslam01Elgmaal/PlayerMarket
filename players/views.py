from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Players

from django.utils.text import slugify

# 🔹 API Imports
from rest_framework import generics
from .serializers import PlayerSerializer


def players_list(request):
    player_list = Players.objects.all()
    
    # pagination
    paginator = Paginator(player_list, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'players/player_list.html', {
        'page_obj': page_obj,
        'players': page_obj.object_list,
        'is_paginated': page_obj.has_other_pages()
    })




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
