from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ContactMessage

# Create your views here.



class ContactView(TemplateView):
    template_name = 'contact/contact.html'