from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})

def film_create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'films/film_create.html', {'form': form})