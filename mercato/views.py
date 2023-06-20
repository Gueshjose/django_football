from django.shortcuts import render,redirect
from .models import Continent,Player, Role ,Team
from .teamForm import TeamForm 
from .playerForm import PlayerForm

# Create your views here.

def home(request):
    return render(request, 'mercato/home/home.html')