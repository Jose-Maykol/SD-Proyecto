from django import forms

from income.models import Income

class IncomeForm(forms.ModelForm):

  class Meta:
    model = Income
    fields = (
      'amount',
      'type'
    )
    
    widgets = {
      'amount' : forms.TextInput(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
    } 
   