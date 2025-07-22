from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'phone_number', 'location']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Number', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location', 'class': 'form-control'}),
        }
