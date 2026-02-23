from django.db import models

# Create your models here.
class Anime(models.Model):
    titol = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    any = models.IntegerField()

    def __str__(self):
        return self.titol


class Personatge(models.Model):
    nom = models.CharField(max_length=200)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='personatges')

    def __str__(self):
        return self.nom
#Oleguer
