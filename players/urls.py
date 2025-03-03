from django.urls import path
from .views import players_list, PlayersDetailView
from django.conf import settings
from django.conf.urls.static import static



app_name = 'players'

urlpatterns = [
    path('', players_list, name='player_list'),  
    path('<int:pk>/', PlayersDetailView.as_view(), name='player_detail'),  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)