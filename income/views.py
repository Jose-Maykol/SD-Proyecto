from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from income.forms import IncomeForm
from income.models import Income


class IncomeCreateView(CreateView):
  model = Income
  form_class = IncomeForm
  template_name = 'create_income.html'
  success_url = '/income/list/'

class IncomeListView(ListView):
  model = Income
  template_name = 'list_income.html'
