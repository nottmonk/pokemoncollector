from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Rarity
from .forms import CaughtForm
from django.shortcuts import render, redirect



# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/index.html',{
        'pokemons': pokemons
    })

def pokemon_details(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    caught_form = CaughtForm
    return render(request, 'pokemon/details.html', {'pokemon': pokemon , 'caught_form': caught_form})



def capture(request, pokemon_id):
    form = CaughtForm(request.POST)

    if form.is_valid():
        new_caught = form.save(commit=False)
        new_caught.pokemon_id = pokemon_id
        new_caught.save()
    return redirect('details', pokemon_id=pokemon_id)


class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    


class PokemonUpdate(UpdateView):
    model = Pokemon
    
    fields = ['name', 'description', 'element']


class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon'




class RarityList(ListView):
    model = Rarity



class RarityDetail(DetailView):
    model = Rarity



class RarityCreate(CreateView):
    model = Rarity
    fields = '__all__'


class RarityUpdate(UpdateView):
    model = Rarity
    fields = ['rarity']

class RarityDelete(DeleteView):
    model = Rarity
    success_url = '/pokemon'







