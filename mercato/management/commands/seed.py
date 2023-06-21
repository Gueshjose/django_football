from django_seed import Seed    
from mercato.models import Team,Player, Role, Continent, Tactics
from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from faker import Faker
from random import randint
from pathlib import Path


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
            seeder.add_entity( Team, 1,{                
                    'name':equipes[randint(0,len(equipes)-1)],
                    'ville':fake.city(),
                    'pays': fake.country(),
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
        
        prenoms_masculins = [
            "Liam", "Noah", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason", "Logan",
            "Alexander", "Ethan", "Jacob", "Michael", "Daniel", "Henry", "Jackson", "Sebastian", "Aiden", "Matthew",
            "Samuel", "David", "Joseph", "Carter", "Owen", "Wyatt", "John", "Jack", "Luke", "Jayden",
            "Dylan", "Grayson", "Levi", "Isaac", "Gabriel", "Julian"
        ]

        prenoms_feminins = [
            "Olivia", "Emma", "Ava", "Sophia", "Isabella", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn",
            "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila", "Aria", "Scarlett",
            "Victoria", "Madison", "Luna", "Grace", "Chloe", "Penelope", "Layla", "Riley", "Zoey", "Nora",
            "Lily", "Eleanor", "Hannah", "Lillian", "Addison", "Aubrey", "Ellie"
        ]

        for team in Team.objects.all() :
            att =int(team.maxATT)
            mid= int(team.maxMID)
            de = int(team.maxDEF)
            g= int(team.maxG)
            r = int(team.maxREM)
            for _ in range(randint(8,14)):  
                roleNB=randint(0,4) 
                if roleNB == 0:
                    role=Role.objects.get(poste='Attaquant')
                    if att <= 0:
                        team=None
                    else :  
                        team=team
                        att= att-1
                elif roleNB == 1:
                    role=Role.objects.get(poste='Millieu')
                    if mid <= 0:
                        team=None
                    else :  
                        team=team
                        mid= mid-1
                elif roleNB == 2:
                    role=Role.objects.get(poste='Defenseur')
                    if de <= 0:
                        team=None
                    else :  
                        team=team
                        de= de-1
                elif roleNB == 3:
                    role=Role.objects.get(poste='Gardien')
                    if g <= 0:
                        team=None
                    else :  
                        team=team
                        g= g-1
                else:
                    role=Role.objects.get(poste='Remplaçant')
                    if r <= 0:
                        team=None
                    else :  
                        team=team
                        r= r-1
                rand=randint(0,1)
                if rand == 0:
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
                        'photo':create_logo_file(),
                        'role': role,
                        'team': team,
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
    