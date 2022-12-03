from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def aboutpage(request):
    return render(request, 'about.html')


def property1(request):
    return render(request, 'property1.html')

class Property(LoginRequiredMixin, ListView):
    model = Property
    template_name = 'propertyPage.html'

@login_required
def contactpage(request):
    return render(request, 'contact.html')


def createproperty(request):
    return render(request, 'createproperty.html')



