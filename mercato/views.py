from django.shortcuts import render,redirect
from .models import Continent,Player, Role ,Team,Tactics
from .teamForm import TeamForm 
from .playerForm import PlayerForm

# Create your views here.

def home(request):
    return render(request, 'mercato/home/home.html')


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