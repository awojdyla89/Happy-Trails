from .models import Trail

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, 'about.html')

class TrailList(ListView):
    model = Trail

class TrailDetail(DetailView):
    model = Trail

class TrailCreate(CreateView):
    model = Trail
    fields = ['name', 'address', 'city', 'state', 'trail_length']

