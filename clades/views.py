from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Species, Genus

class SpeciesListView(ListView):
    model = Species

class GenusListView(ListView):
    model = Genus
