from django.shortcuts import render,redirect
from .models import Continent,Player, Role ,Team,Tactics
from .teamForm import TeamForm 
from .playerForm import PlayerForm
from django.db.models import Q
from django.core.files.storage import default_storage

# Create your views here.

def home(request):
    # Récuppération des teams full
    fullTeam=[]
    # 2 Team non remplie
    notFullTeam=[]
    i=0
    for team in Team.objects.prefetch_related('continent').all():
        nb_att = Player.objects.prefetch_related('team','role').filter(role__poste='Attaquant',team_id = team.id).count()
        nb_mid = Player.objects.prefetch_related('team','role').filter(role__poste='Millieu',team_id = team.id).count()
        nb_def = Player.objects.prefetch_related('team','role').filter(role__poste='Defenseur',team_id = team.id).count()
        nb_gk = Player.objects.prefetch_related('team','role').filter(role__poste='Gardien',team_id = team.id).count()
        nb_rem = Player.objects.prefetch_related('team','role').filter(role__poste='Remplaçant',team_id = team.id).count()

        if nb_att == team.maxATT and nb_mid == team.maxMID and nb_def == team.maxDEF and nb_gk == team.maxG and nb_rem == team.maxREM:
            fullTeam.append(team)
        elif i!=2 and not(nb_att== team.maxATT and nb_mid == team.maxMID and nb_def == team.maxDEF and nb_gk == team.maxG and nb_rem == team.maxREM):
            notFullTeam.append(team)
            i+=1  

    # Team Europe
    teamEurope=Team.objects.prefetch_related('continent').filter(continent__name='Europe')
    
    # Team non Europ
    teamNotEurope=Team.objects.prefetch_related('continent').filter(~Q(continent__name='Europe'))
    context=locals()
    print(context)
    return render(request, 'mercato/home/home.html', context)

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
    if player.photo:
        # Supprimer le photo du système de fichiers
        default_storage.delete(player.photo.path)

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
            team.maxREM= int(request.POST.get('maxREM',0))
            team.composition= request.POST.get('composition','X')
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
    team=Team.objects.get(id=id)
    if team.logo:
        # Supprimer le logo du système de fichiers
        default_storage.delete(team.logo.path)

    # Supprimer la team
    team.delete()
    return redirect('back')