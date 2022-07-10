from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from expenses.forms import ExpenseForm

from expenses.models import Expenses

class ExpenseCreateView(CreateView):

  model = Expenses
  form_class = ExpenseForm
  template_name = 'create_expense.html'
  success_url = '/expenses/list/'

class ExpenseListView(ListView):

  model = Expenses
  template_name = 'list_expense.html'