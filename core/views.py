from django.shortcuts import render
from .models import Gif

# Create your views here.

def home(request):
    gifs = Gif.objects.all()
    return render(request, 'core/home.html', {'gifs': gifs})