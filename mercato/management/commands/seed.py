from django_seed import Seed    
from mercato.models import Team,Player, Role, Continent
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
        formation=[{'att':4,"mid":4,"def":2},{'att':4,"mid":3,"def":3},{'att':4,"mid":2,"def":4},{'att':4,"mid":5,"def":1},{'att':4,"mid":1,"def":5},
                    {'att':5,"mid":3,"def":2},{'att':5,"mid":4,"def":1},{'att':5,"mid":2,"def":3},{'att':5,"mid":1,"def":4},
                    {'att':6,"mid":2,"def":2},{'att':6,"mid":3,"def":1},{'att':6,"mid":1,"def":3},{'att':3,"mid":4,"def":3},{'att':3,"mid":3,"def":4},{'att':3,"mid":5,"def":2},{'att':3,"mid":2,"def":5},
                    {'att':3,"mid":6,"def":1},{'att':3,"mid":1,"def":6},{'att':2,"mid":4,"def":4},{'att':2,"mid":3,"def":5},{'att':2,"mid":5,"def":3},
                    {'att':2,"mid":2,"def":6},{'att':2,"mid":6,"def":2},{'att':2,"mid":1,"def":7},{'att':2,"mid":7,"def":1},
                    {'att':1,"mid":5,"def":4},{'att':1,"mid":4,"def":5},{'att':1,"mid":3,"def":6},{'att':1,"mid":6,"def":3},{'att':1,"mid":2,"def":7},{'att':1,"mid":7,"def":2},{'att':1,"mid":1,"def":8},{'att':1,"mid":8,"def":1},
                    {'att':7,"mid":2,"def":1},{'att':7,"mid":1,"def":2},{'att':8,"mid":1,"def":1},]
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
        
        for _ in range(20):   
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
                    'age': randint(16,35),
                    'email': fake.ascii_email() ,
                    'phone': fake.phone_number(),
                    'photo':create_logo_file(),
                    'role': Role.objects.order_by('?').first(),
                    'team': None,
            })
            
            

        inserted_pks = seeder.execute()
        print(inserted_pks)

    
def create_logo_file():
        # Créez un fichier image factice avec un nom aléatoire
        image_name = fake.file_name(extension='jpg')
        image_path = Path('static/images/') / image_name

        # Créez un fichier temporaire pour l'image
        image_temp_file = ImageFile(open('static/images/random.png', 'rb'))

        # Copiez le fichier temporaire dans le dossier 'images'
        with image_path.open('wb') as destination:
            for chunk in image_temp_file.chunks():
                destination.write(chunk)

        return str(image_path)[7:] 

def create_image_file():
        # Créez un fichier image factice avec un nom aléatoire
        image_name = fake.file_name(extension='jpg')
        image_path = Path('static/images/') / image_name

        # Créez un fichier temporaire pour l'image
        image_temp_file = ImageFile(open('static/images/random.png', 'rb'))

        # Copiez le fichier temporaire dans le dossier 'images'
        with image_path.open('wb') as destination:
            for chunk in image_temp_file.chunks():
                destination.write(chunk)

        return str(image_path)[7:]    
    