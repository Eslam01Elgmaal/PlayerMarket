from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import (
    players_list,
    PlayersDetailView,
    PlayerListAPI,
    PlayerDetailAPI,
)

app_name = 'players'

urlpatterns = [
    path('', players_list, name='player_list'),
    path('<slug:slug>', PlayersDetailView.as_view(), name='player_detail'),

    # API endpoints
    path('api/', PlayerListAPI.as_view(), name='player_list_api'),
    path('api/<int:pk>/', PlayerDetailAPI.as_view(), name='player_detail_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
