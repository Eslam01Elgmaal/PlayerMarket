
from django.urls import path
from .views import logout_view, signup_view

urlpatterns = [
    path('auth/', signup_view, name='auth'), 
    path('logout/', logout_view, name='logout'),
]
