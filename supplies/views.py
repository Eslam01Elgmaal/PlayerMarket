from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TShirt
# Create your views here.

def tshirt_list(request):
    tshirt = TShirt.objects.all()

    return render(request, 'tshirt/tshirt_list.html', {'tshirt': tshirt})




class TshirtDetailView(DetailView):
    model = TShirt
    template_name = 'tshirt/tshirt_detail.html'
    context_object_name = 'tshirt'
    

