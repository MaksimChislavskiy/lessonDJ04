from django.shortcuts import render, redirect

from .models import Film
from .forms import FilmForm


def films(request):
    films = Film.objects.all()
    return render(request, 'films/films.html', {'films': films})

def create_film(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(films)
        else:
            error = "Данные были заполнены некорректно"
    form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form, 'error': error})
