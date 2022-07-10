from django import forms
from expenses.models import Expenses


class ExpenseForm(forms.ModelForm):

  class Meta:

    model = Expenses
    fields = (
      'amount',
      'category'
    )

    widgets = {
      'amount' : forms.TextInput(attrs={'class': 'form-control'}),
      'category' : forms.Select(attrs={'class': 'form-control'})
    }