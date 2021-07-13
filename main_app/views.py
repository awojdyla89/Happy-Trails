from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from .models import Trail, Comment, Amenity
from .forms import CommentForm
from django.urls import reverse_lazy, reverse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, 'about.html')

class TrailList(ListView):
    model = Trail

@login_required
def trails_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    comment_form = CommentForm()
    return render(request, 'trails/detail.html', {
        'trail': trail, 'comment_form': comment_form
    })

class TrailCreate(LoginRequiredMixin, CreateView):
    model = Trail
    fields = ['name', 'address', 'city', 'state', 'trail_length', 'amenities']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/trails/'


class TrailUpdate(LoginRequiredMixin, UpdateView):
    model = Trail
    fields = ['name', 'address', 'city', 'state', 'trail_length', 'amenities']


class TrailDelete(LoginRequiredMixin, DeleteView):
    model = Trail
    success_url = '/trails/'

@login_required
def add_comment(request, trail_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.trail_id = trail_id
        form.instance.user = request.user
        new_comment.save()
    return redirect('detail', trail_id=trail_id)

class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = ['description']

@login_required
def delete_comment(request, trail_id, comment_id):
  Comment.objects.get(id=comment_id).delete()
  return redirect('detail', trail_id=trail_id)
  #return reverse('detail', kwargs={'trail_id': self.object.trail_id})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
