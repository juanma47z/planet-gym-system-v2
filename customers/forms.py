from django import forms
from .models import Customers

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }