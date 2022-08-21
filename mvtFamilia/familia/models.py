from django.db import models


class Parientes(models.Model):
    nombre=models.CharField(max_length=20)
    parentesco=models.CharField(max_length=20)
    edad=models.IntegerField()
    fecha=models.DateField()
       
    
    #datetime.datetime.today()
