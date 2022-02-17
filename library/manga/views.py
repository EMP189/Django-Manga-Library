from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Manga
from .forms import AddMangaForm
# Create your views here.

def index(req):
    # NOTE_TO_SELF: no need to make the templates be inside another folder inside templates
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')
def show(req):
    data={'manga':Manga.objects.all()}
    return render(req, 'show.html', data)

def createManga(req):
    if req.method == 'POST':
        manga = AddMangaForm(req.POST)
        if manga.is_valid():
            manga.save()
            manga_name = manga.cleaned_data.get('name')
            messages.success(req, f'{manga_name} has been added succesfully')
            return redirect('manga-index')
    else:
        form = AddMangaForm()
    data = {'form': form}
    return render(req, 'new.html', data)