from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import TShirt, Size, Order 
from .forms import OrderForm

def tshirt_list(request):
    tshirt = TShirt.objects.all()

    return render(request, 'tshirt/tshirt_list.html', {'tshirts': tshirt})




class TshirtDetailView(DetailView):
    model = TShirt
    template_name = 'tshirt/tshirt_detail.html'
    context_object_name = 'tshirt'
    






def create_order(request, tshirt_id):
    if request.method != 'POST':
        return JsonResponse({
            'success': False,
            'error': 'Invalid request.'
        }, status=400)

    tshirt = get_object_or_404(TShirt, id=tshirt_id)

    form = OrderForm(request.POST)

    if not form.is_valid():
        return JsonResponse({
            'success': False,
            'errors': form.errors
        }, status=400)

    size_id = request.POST.get('size')

    if not size_id:
        return JsonResponse({
            'success': False,
            'error': 'Please select a size.'
        }, status=400)

    size = get_object_or_404(Size, id=size_id)

    if not tshirt.size.filter(id=size.id).exists():
        return JsonResponse({
            'success': False,
            'error': 'This size is not available.'
        }, status=400)

    order = form.save(commit=False)
    order.tshirt = tshirt
    order.size = size
    order.price = tshirt.price
    order.save()

    return JsonResponse({
        'success': True,
        'message': 'Booking Confirmed!'
    })

