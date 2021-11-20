from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Horse
from .forms import FeedingForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def horses_index(request):
  horses = Horse.objects.all()
  return render(request, 'horses/index.html', { 'horses': horses })

def horses_detail(request, horse_id):
  horse = Horse.objects.get(id=horse_id)
  feeding_form = FeedingForm()
  return render(request, 'horses/detail.html', {
    'horse': horse, 'feeding_form': feeding_form
  })

def add_feeding(request, horse_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.horse_id = horse_id
    new_feeding.save()
  return redirect('horses_detail', horse_id=horse_id)



class HorseCreate(CreateView):
  model = Horse
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/horses/'

class HorseUpdate(UpdateView):
  model = Horse
  fields = ['breed', 'description', 'age']

class HorseDelete(DeleteView):
  model = Horse
  success_url = '/horses/'

