# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings 


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(request, 'تم إرسال الرسالة بنجاح!')
            return redirect('contact:contact')

    else:
    
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

