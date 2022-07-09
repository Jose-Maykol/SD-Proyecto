from django import forms
from django.forms import widgets

from income.models import Income

class IncomeForm(forms.ModelForm):

  class Meta:
    model = Income
    fields = (
      'amount',
      'category'
    )
    
    widgets = {
      'amount' : forms.TextInput(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
    } 
   