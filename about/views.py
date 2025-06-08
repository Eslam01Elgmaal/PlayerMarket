from django.shortcuts import render
from django.views.generic import ListView
from .models import About

# Create your views here.



class AboutView(ListView):
    model = About
    template_name = 'about/about_detail.html'
    context_object_name = 'about_list'
