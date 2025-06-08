from django.shortcuts import render
from django.views.generic import DetailView
from .models import Home, Why
# Create your views here.


class HomeView(DetailView):

    model = Home
    template_name = 'home/home_detail.html'
    context_object_name = 'home'



    def get_object(self, queryset=None):
        return Home.objects.first()




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['why_list'] = Why.objects.all() 
        return context