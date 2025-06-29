from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import TShirt, Purchase
# Create your views here.

def tshirt_list(request):
    tshirt = TShirt.objects.all()

    return render(request, 'tshirt/tshirt_list.html', {'tshirts': tshirt})




class TshirtDetailView(DetailView):
    model = TShirt
    template_name = 'tshirt/tshirt_detail.html'
    context_object_name = 'tshirt'
    
def buy_tshirt(request, pk):
    if request.method == 'POST':
        tshirt = get_object_or_404(TShirt, pk=pk)
        size = request.POST.get('size')
        Purchase.objects.create(tshirt=tshirt, size=size)
        messages.success(request, 'تم شراء التيشيرت بنجاح ✅')
        return redirect('tshirt:tshirt_detail', pk=tshirt.pk)