from django.shortcuts import render,redirect
from .models import Continent,Player, Role ,Team
from .teamForm import TeamForm 
from .playerForm import PlayerForm

# Create your views here.

def home(request):
    return render(request, 'mercato/home/home.html')

def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlayerForm()
    return render(request, 'mercato/admin/create_player.html', {'form': form})

def update_player(request, id):
    player = Player.objects.get(id=id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'mercato/admin/update_player.html', {'form': form})

def delete_player(request, id):
    player = Player.objects.get(id=id)
    player.delete()
    return redirect('home')