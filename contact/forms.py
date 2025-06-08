# forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-field', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-field', 'placeholder': 'Message', 'rows': 5}),
        }
