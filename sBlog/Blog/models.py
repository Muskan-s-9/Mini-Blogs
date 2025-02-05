from django.db import models

# Create your models here.

class Post(models.Model):
    
    tittle = models.CharField(max_length=200)
    desc  =  models.CharField(max_length=700) 

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    message = models.CharField(max_length=200)