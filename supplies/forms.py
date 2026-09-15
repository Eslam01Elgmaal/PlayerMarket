from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer_name',
            'customer_email',
            'customer_phone',
            'address',
        ]

        widgets = {
            'customer_name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'order-input',
            }),
            'customer_email': forms.EmailInput(attrs={
                'placeholder': 'Your Email',
                'class': 'order-input',
            }),
            'customer_phone': forms.TextInput(attrs={
                'placeholder': 'Your Phone',
                'class': 'order-input',
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Your Address',
                'class': 'order-input',
                'rows': 3,
            }),
        }