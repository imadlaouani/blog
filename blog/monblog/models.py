
# Create your models here.
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Auteur(models.Model):

    numAuteur = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=42)
    


class Post(models.Model):
	idpost = models.AutoField(primary_key=True)
	titre = models.CharField(max_length=100)
	description = models.TextField(null=True)
	date = models.DateTimeField(default=timezone.now,verbose_name="Date de publication")
	auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)

   # auteur = models.ForeignKey(Auteur,null=True,blank=True, on_delete=models.CASCADE)




