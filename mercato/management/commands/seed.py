from django_seed import Seed    
from mercato.models import Team,Player, Role, Continent, Tactics
from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from faker import Faker
from random import randint
from pathlib import Path
import os
from django.conf import settings

fake = Faker()

class Command(BaseCommand):
    help = 'Making Seed'
    
    Team.objects.all().delete()
    Role.objects.all().delete()
    Player.objects.all().delete()
    Continent.objects.all().delete()
    Tactics.objects.all().delete()
    
                
    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        delete_all_images()
        # Seed for continents
        
        continents = ['Europe', 'Oceanie','Asie','Afrique','Amerique']
        for continent in continents: 
            seeder.add_entity(Continent, 1, {
                'name' : continent,
            }
        )
       
        #    Seed for Roles
        
        roles = ['Attaquant', 'Millieu','Defenseur','Gardien','Remplaçant']
        for role in roles: 
            seeder.add_entity(Role, 1, {
                'poste' : role,
            }
        )
        formation=[{'att':4,"mid":4,"def":2}, #
                   {'att':4,"mid":3,"def":3},#
                   {'att':4,"mid":2,"def":4},#
                   {'att':4,"mid":5,"def":1},#
                   {'att':4,"mid":1,"def":5},#
                    {'att':5,"mid":3,"def":2},#
                    {'att':5,"mid":4,"def":1},#
                    {'att':5,"mid":2,"def":3},#
                    {'att':5,"mid":1,"def":4},#
                    {'att':3,"mid":4,"def":3},#
                    {'att':3,"mid":3,"def":4},#
                    {'att':3,"mid":5,"def":2},#
                    {'att':3,"mid":2,"def":5},#
                    {'att':2,"mid":4,"def":4},#
                    {'att':2,"mid":3,"def":5},#
                    {'att':2,"mid":5,"def":3},#
                    {'att':1,"mid":5,"def":4},#
                    {'att':1,"mid":4,"def":5},]
        inserted_pks = seeder.execute()
        print(inserted_pks)
        
        # Seed for Teams
        
        equipes = [
    "Galácticos United",
    "Emperor FC",
    "Silver Angels",
    "Supreme Beats",
    "Royal Titans",
    "Eternal Legends",
    "Imperial Warriors",
    "Phoenix Rising",
    "United Monarchs",
    "Golden Panthers",
    "Cosmic Strikers",
    "Thunder Dragons",
    "Diamond Eagles",
    "Celestial Lions",
    "Sovereign Knights",
    "Majestic Falcons",
    "Victorious Spartans",
    "Steel Giants",
    "All-Star Titans",
    "Champions United",
    "Epic Thunderbolts",
    "Phoenix Knights",
    "Regal Jaguars",
    "Golden Warriors",
    "Silver Stars",
    "Supreme Legends",
    "Imperial Rangers",
    "Royal Eagles",
    "Eternal Titans",
    "Galactic Strikers",
    "Emperor United",
    "Silver Angels",
    "Supreme Beats",
    "Royal Titans",
    "Eternal Legends",
    "Imperial Warriors",
    "Phoenix Rising",
    "United Monarchs",
    "Golden Panthers",
    "Cosmic Strikers",
    "Thunder Dragons",
    "Diamond Eagles",
    "Celestial Lions",
    "Sovereign Knights",
    "Majestic Falcons",
    "Victorious Spartans",
    "Steel Giants",
    "All-Star Titans",
    "Champions United",
    "Epic Thunderbolts",
    "Phoenix Knights",
    "Regal Jaguars",
    "Golden Warriors",
    "Silver Stars",
    "Supreme Legends",
    "Imperial Rangers",
    "Royal Eagles",
    "Eternal Titans",
    "Galactic Strikers",
    "Emperor United",
    "Silver Angels",
    "Supreme Beats",
    "Royal Titans",
    "Eternal Legends",
    "Imperial Warriors",
    "Phoenix Rising",
    "United Monarchs",
    "Golden Panthers",
    "Cosmic Strikers",
    "Thunder Dragons",
    "Diamond Eagles",
    "Celestial Lions",
    "Sovereign Knights",
    "Majestic Falcons",
    "Victorious Spartans",
    "Steel Giants",
    "All-Star Titans",
    "Champions United",
    "Epic Thunderbolts",
    "Phoenix Knights",
    "Regal Jaguars",
    "Golden Warriors",
    "Silver Stars",
    "Supreme Legends",
    "Imperial Rangers",
    "Royal Eagles",
    "Eternal Titans",
    "Galactic Strikers",
    "Emperor United",
    "Silver Angels",
    "Supreme Beats",
    "Royal Titans",
    "Eternal Legends",
    "Imperial Warriors",
    "Phoenix Rising",
    "United Monarchs",
    "Golden Panthers",
    "Cosmic Strikers",
    "Thunder Dragons",
    "Diamond Eagles",
    "Celestial Lions",
    "Sovereign Knights",
    "Majestic Falcons",
    "Victorious Spartans",
    "Steel Giants",
    "All-Star Titans",
    "Champions United",
    "Epic Thunderbolts",
    "Phoenix Knights",
    "Regal Jaguars",
    "Golden Warriors",
    "Silver Stars",
    "Supreme Legends",
    "Imperial Rangers",
    "Royal Eagles",
    "Eternal Titans",
    "Galactic Strikers"
]
        
        for _ in range(5):   
            rand=randint(0,len(formation)-1)
            compo=randint(0,2)
            if compo == 0:
                cp="M"
            elif compo==1:
                cp="F"
            else:
                cp="X"   
            seeder.add_entity( Team, 1,{                
                    'name':equipes[randint(0,len(equipes)-1)],
                    'ville':fake.city(),
                    'pays': fake.country(),
                    'composition':cp,
                    'maxATT':formation[rand]['att'],
                    'maxMID':formation[rand]['mid'],
                    'maxDEF':formation[rand]['def'],
                    'maxG':1,
                    'maxREM':randint(0, 10),
                    'logo':create_logo_file(),
                    'continent': Continent.objects.order_by('?').first(),
            })
        inserted_pks = seeder.execute()
        print(inserted_pks)
        

        for team in Team.objects.all() :
            att =int(team.maxATT)
            mid= int(team.maxMID)
            de = int(team.maxDEF)
            g= int(team.maxG)
            r = int(team.maxREM)
            for _ in range(randint(11,20)):  
                roleNB=randint(0,3) 
                if roleNB == 0:
                    role=Role.objects.get(poste='Attaquant')
                    if att <= 0:
                        if r <= 0:
                            t=None
                        else :  
                            role=Role.objects.get(poste='Remplaçant')
                            t=team
                            r= r-1
                    else :  
                        t=team
                        att= att-1
                elif roleNB == 1:
                    role=Role.objects.get(poste='Millieu')
                    if mid <= 0:
                        if r <= 0:
                            t=None
                        else :  
                            role=Role.objects.get(poste='Remplaçant')
                            t=team
                            r= r-1
                    else :  
                        t=team
                        mid= mid-1
                elif roleNB == 2:
                    role=Role.objects.get(poste='Defenseur')
                    if de <= 0:
                        if r <= 0:
                            t=None
                        else :  
                            role=Role.objects.get(poste='Remplaçant')
                            t=team
                            r= r-1
                    else :  
                        t=team
                        de= de-1
                else:
                    role=Role.objects.get(poste='Gardien')
                    if g <= 0:
                        if r <= 0:
                            t=None
                        else :  
                            role=Role.objects.get(poste='Remplaçant')
                            t=team
                            r= r-1
                    else :  
                        t=team
                        g= g-1
                    
                    
                rand=randint(0,1)
                if (rand == 0 and team.composition == "X" ) or (team.composition == "M"):
                    gender ='H'
                    fName=fake.first_name_male()
                else:
                    gender ='F'
                    fName=fake.first_name_female()
                seeder.add_entity( Player, 1,{                
                        'last_name': fake.last_name(),
                        'first_name':fName,
                        'country': fake.country(),
                        'gender':gender,
                        'age': randint(16,35),
                        'email': fake.ascii_email() ,
                        'phone': fake.phone_number(),
                        'photo':create_image_file(),
                        'role': role,
                        'team': t,
                })
            
        formations=[{'name':"1-4-5","image":'formation/1-4-5.png'},
                {'name':"1-5-4","image":'formation/1-5-4.png'},
                {'name':"2-3-5","image":'formation/2-3-5.png'},
                {'name':"2-5-3","image":'formation/2-5-3.png'},
                {'name':"2-4-4","image":'formation/2-4-4.png'},
                {'name':"3-3-4","image":'formation/3-3-4.png'},
                {'name':"3-2-5","image":'formation/3-2-5.png'},
                {'name':"3-4-3","image":'formation/3-4-3.png'},
                {'name':"3-5-2","image":'formation/3-5-2.png'},
                {'name':"4-1-5","image":'formation/4-1-5.png'},
                {'name':"4-2-4","image":'formation/4-2-4.png'},
                {'name':"4-3-3","image":'formation/4-3-3.png'},
                {'name':"4-5-1","image":'formation/4-5-1.png'},
                {'name':"5-1-4","image":'formation/5-1-4.png'},
                {'name':"5-2-3","image":'formation/5-2-3.png'},
                {'name':"5-3-2","image":'formation/5-3-2.png'},
                {'name':"5-4-1","image":'formation/5-4-1.png'},
                {'name':"5-4-1","image":'formation/5-4-1.png'},
        ]
        
        for form in formations:
            seeder.add_entity(Tactics,1,{
                'name':form['name'],
                'image':form['image'],
            })

        inserted_pks = seeder.execute()
        print(inserted_pks)

def delete_all_images():
        # Chemin du répertoire des images
        images_dir = os.path.join(settings.MEDIA_ROOT, 'images/')
        print(images_dir)
        # Parcourir tous les fichiers du répertoire
        for file_name in os.listdir(images_dir):
            if file_name != "random.png" and  file_name != "logo.png":
                # Construire le chemin complet du fichier
                file_path = os.path.join(images_dir, file_name)

                # Vérifier si c'est un fichier (et non un sous-répertoire)
                if os.path.isfile(file_path):
                    # Supprimer le fichier
                    os.remove(file_path)
                    
def create_logo_file():
        # Créez un fichier image factice avec un nom aléatoire
        image_name = fake.file_name(extension='png')
        image_path = Path('static/images/') / image_name

        # Créez un fichier temporaire pour l'image
        image_temp_file = ImageFile(open('static/images/logo.png', 'rb'))

        # Copiez le fichier temporaire dans le dossier 'images'
        with image_path.open('wb') as destination:
            for chunk in image_temp_file.chunks():
                destination.write(chunk)

        return str(image_path)[7:] 

def create_image_file():
        # Créez un fichier image factice avec un nom aléatoire
        image_name = fake.file_name(extension='png')
        image_path = Path('static/images/') / image_name

        # Créez un fichier temporaire pour l'image
        image_temp_file = ImageFile(open('static/images/random.png', 'rb'))

        # Copiez le fichier temporaire dans le dossier 'images'
        with image_path.open('wb') as destination:
            for chunk in image_temp_file.chunks():
                destination.write(chunk)

        return str(image_path)[7:]    
    