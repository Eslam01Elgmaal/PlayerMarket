from django.urls import path
from .views import tshirt_list, TshirtDetailView



app_name = 'tshirt'

urlpatterns = [
    path('', tshirt_list, name='tshirt_list'),  
    path('<int:pk>/', TshirtDetailView.as_view(), name='tshirt_detail'),  
]
