from django.shortcuts import render
from django.views.generic import DetailView
from .models import Coaches

# Create your views here.


def coaches_list(request):
    coaches = Coaches.objects.all()

    return render(request, 'coaches/coaches_list.html', {'coaches': coaches})



class CoachesDetailView(DetailView):
    model = Coaches
    template_name = 'coaches/coaches_detail.html'
    context_object_name = 'coach'