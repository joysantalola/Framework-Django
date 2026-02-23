from django.shortcuts import render, redirect
from .models import Anime
from .forms import AnimeForm
from django.shortcuts import get_object_or_404
from .forms import PersonatgeForm

def afegir_personatge(request):
    if request.method == 'POST':
        form = PersonatgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('llista_animes')
    else:
        form = PersonatgeForm()
    return render(request, 'afegir_personatge.html', {'form': form})
def llista_animes(request):
    animes = Anime.objects.all()
    return render(request, 'llista_animes.html', {'animes': animes})

def afegir_anime(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('llista_animes')
    else:
        form = AnimeForm()

    return render(request, 'afegir_anime.html', {'form': form})

def editar_anime(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        form = AnimeForm(request.POST, instance=anime)
        if form.is_valid():
            form.save()
            return redirect('llista_animes')
    else:
        form = AnimeForm(instance=anime)
    return render(request, 'afegir_anime.html', {'form': form})

def eliminar_anime(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    anime.delete()
    return redirect('llista_animes')

#Oleguer
