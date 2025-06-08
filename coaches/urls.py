from django.urls import path
from .views import coaches_list, CoachesDetailView


app_name = 'coaches'

urlpatterns = [
    path('', coaches_list, name='coaches_list'),  

    path('<int:pk>/', CoachesDetailView.as_view(), name='coach-detail'),  
]


