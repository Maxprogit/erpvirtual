from django.db import models



# Create your models here.

class Usuario(models.Model):
    Email = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    
    
    
    
   
    


    
    
