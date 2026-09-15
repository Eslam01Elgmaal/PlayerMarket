from django.urls import path
from . import views

app_name = 'tshirt'

urlpatterns = [
    path('', views.tshirt_list, name='tshirt_list'),
    path(
        '<int:pk>/',
        views.TshirtDetailView.as_view(),
        name='tshirt_detail'
    ),
    path(
        'order/<int:tshirt_id>/',
        views.create_order,
        name='create_order'
    ),
]