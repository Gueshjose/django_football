from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Role(models.Model):
    class Role(models.TextChoices):
        Attaquant = "Attaquant"
        Millieu = "Millieu"
        Défenseur = "Défenseur"
        Gardien = "Gardien"
        Remplaçant= "Remplaçant"
    
    poste=models.CharField(choices=Role.choices, max_length=10)
    img=models.ImageField(upload_to='images/', default='None')
    
    def __str__(self):
        return self.poste


class Continent(models.Model):
    class Continent(models.TextChoices):
        Europe= "Europe"
        Asie= "Asie"
        Afrique= "Afrique"
        Amerique = "Amerique"
        Oceanie = "Oceanie" 
    name=models.CharField(choices=Continent.choices, max_length=10)
    
    def __str__(self):
        return self.name

class Team(models.Model):
    class Compo(models.TextChoices):
        Masculine='M'
        Feminine="F"
        Mixte='X'
    name=models.CharField(max_length=20)
    ville=models.CharField(max_length=20)
    pays=models.CharField(max_length=20)
    composition=models.CharField(choices=Compo.choices,max_length=1, default="X")
    maxATT=models.IntegerField()
    maxMID=models.IntegerField()
    maxDEF=models.IntegerField()
    maxG=models.IntegerField()
    maxREM=models.IntegerField()
    logo=models.ImageField(upload_to='images/')
    continent=models.ForeignKey(Continent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Player(models.Model):
    class Gender(models.TextChoices):
        Homme= "H"
        Femme='F'
    last_name=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    age=models.IntegerField(validators=[MinValueValidator(16),MaxValueValidator(35)])
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    gender=models.CharField(choices=Gender.choices, max_length=1)
    country=models.CharField(max_length=20)
    photo=models.ImageField(upload_to='images/')
    role=models.ForeignKey(Role, on_delete=models.CASCADE)
    team=models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    
    def __str__(self):
        return  self.id

class Tactics(models.Model):
    name=models.CharField(max_length=5)
    image=models.ImageField(upload_to='formation/')
    
    def __str__(self):
        return  self.name