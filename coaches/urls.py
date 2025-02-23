from django.urls import path
from .views import coaches_lsit, CoachesDetailView


app_name = 'coaches'

urlpatterns = [
    path('', coaches_lsit, name='coaches_list'),  

    path('<int:pk>/', CoachesDetailView.as_view(), name='coaches_detail'),  
]


