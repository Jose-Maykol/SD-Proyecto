from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from users.forms import UserForm, UserLoginForm

class userRegister(CreateView):

  form_class = UserForm
  template_name = 'register.html'
  success_url = '/'

  def form_valid(self, form):
    form.save(commit = False)
    return super().form_valid(form)


class userLogin(LoginView):
  
  template_name = 'login.html'
  form_class = UserLoginForm
  success_url = reverse_lazy('home')
