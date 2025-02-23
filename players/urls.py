from django.urls import path
from .views import players_list, PlayersDetailView



app_name = 'players'

urlpatterns = [
    path('', players_list, name='player_list'),  
    path('<int:pk>/', PlayersDetailView.as_view(), name='player_detail'),  
]
