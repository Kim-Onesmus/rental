from django.shortcuts import render
from .forms import CreatedUser
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CreatedUser
    template_name = 'signup.html'
    success_url = reverse_lazy('login')