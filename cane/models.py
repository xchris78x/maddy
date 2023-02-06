from django.db import models
# Create your models here.


class Foto(models.Model):
    immagine = models.ImageField()
    descrizione = models.TextField()
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Blog(models.Model):
    titolo = models.CharField(max_length=100)
    inserzione = models.TextField()
    data = models.DateField()
    
    def __str__(self):
         return self.titolo 

from django.db import models

class HomePage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()