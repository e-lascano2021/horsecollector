from django.shortcuts import render
from django.http import HttpResponse

class Horse: 
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

horses = [
  Horse('Dynasty', 'mustang', 'Kinda rude.', 3),
  Horse('Jewl', 'mustang', 'fast as heck', 1),
  Horse('Epona', 'appaloosa', 'beautiful maine', 4),
  Horse('Gerald', 'arabian horse', 'Neighs loudly.', 6)
]


def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def horses_index(request):
  return render(request, 'horses/index.html', { 'horses': horses })