from django.db import models

# Create your models here.
class Client(models.Model):
    nom_complet = models.CharField(max_length=255)
    password = models.CharField(max_length=4)

    def __str__(self):
        return self.nom_complet