from django.shortcuts import render,redirect
from .models import Continent,Player, Role ,Team,Tactics
from .teamForm import TeamForm 
from .playerForm import PlayerForm

# Create your views here.

def home(request):
    return render(request, 'mercato/home/home.html')

def back(request):
    players=Player.objects.prefetch_related('role','team').all()
    teams=Team.objects.prefetch_related('continent').all()
    context=locals()
    return render(request,'mercato/admin/home.html',context)

def create_player(request):
    role = Role.objects.all()
    team = Team.objects.all()
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlayerForm()
    context = locals()
    return render(request, 'mercato/admin/create_player.html', context)

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


def players(request):
    player = Player.objects.all()
    continent = Continent.objects.all()
    role = Role.objects.all()
    team = Team.objects.all()
    context = {
        'player': player,
        'continent': continent,
        'role': role,
        'team': team,
    }
    return render(request, 'mercato/admin/players.html', context)

def show_player(request, id):
    player = Player.objects.get(id=id)
    return render(request, 'mercato/home/show_player.html', {'player': player})

def store_team(request):
    tactics = Tactics.objects.all()
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)   
        if form.is_valid():
            team = form.save(commit=False)
            team.maxATT = int(request.POST.get('tactic', '')[0])
            team.maxMID = int(request.POST.get('tactic', '')[2])
            team.maxDEF = int(request.POST.get('tactic', '')[4])
            team.maxG = 1
            team.save()
            return redirect('back')
        else:
            print(form.errors)
    else:
        form = TeamForm()
    context=locals()
    return render(request,'mercato/admin/form_team.html', context)

def show_team(request,id):
    team=Team.objects.prefetch_related('continent').get(id=id)
    att=Player.objects.filter(team__id=id).filter(role__poste="Attaquant")
    mid=Player.objects.filter(team__id=id).filter(role__poste="Millieu")
    df=Player.objects.filter(team__id=id).filter(role__poste="Défenseur")
    g=Player.objects.filter(team__id=id).filter(role__poste="Gardien")
    r=Player.objects.filter(team__id=id).filter(role__poste="Remplaçant")
    context=locals()
    return render(request,'mercato/home/show_team.html', context)

def update_team(request,id):
    team=Team.objects.prefetch_related('continent').get(id=id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)   
        if form.is_valid():
            form.save()
            return redirect('back')
        else:
            print(form.errors)
    else:
        form = TeamForm(instance=team)
    context=locals()
    return render(request,'mercato/admin/update_team.html', context)

def delete_team(request,id):
    Team.objects.get(id=id).delete()
    return redirect('back')
