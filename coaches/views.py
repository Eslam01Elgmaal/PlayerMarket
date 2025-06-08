from django.shortcuts import render
from django.core.paginator import Paginator

from django.views.generic import DetailView
from .models import Coaches

# Create your views here.


def coaches_list(request):
    coaches_list = Coaches.objects.all()

     # pagination
    paginator = Paginator(coaches_list, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    


    return render(request, 'coaches/coaches_list.html', { 'coaches': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),})



class CoachesDetailView(DetailView):
    model = Coaches
    template_name = 'coaches/coaches_detail.html'
    context_object_name = 'coach'