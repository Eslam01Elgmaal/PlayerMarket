from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Home
# Create your views here.


class HomeView(TemplateView):

    model = Home
    template_name = 'home/home_detail.html'
    context_object_name = 'home'

