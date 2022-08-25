from http.client import HTTPResponse
from django.shortcuts import render
from .models import Parientes
import datetime
from django.http import HttpResponse
from django.template import Context, Template

def papa(request):
    pariente1=Parientes(nombre="Pepe", parentesco ="Padre", edad = "65", fecha=datetime.datetime.today())
    pariente1.save()
    return render(request, "familia/papa.html")

def mama(request):
    pariente2=Parientes(nombre="Pepa", parentesco ="Madre", edad = "61", fecha=datetime.datetime.today())
    pariente2.save()
    return render(request, "familia/mama.html")

def hijo(request):
    pariente3=Parientes(nombre="Pepito", parentesco ="Hijo", edad = "11", fecha=datetime.datetime.today())
    pariente3.save()
    return render(request, "familia/hijo.html")

def inicio(request):

    #fecha=datetime.datetime.today()
    #diccionario={"fecha":fecha,}
    #mihtml=open("C:/Users/Lucho/Desktop/MVT_PROYECTO/mvtFamilia/Plantillas/template1.html")
    #plantilla=Template(mihtml.read())
    #mihtml.close()
    #contexto=Context(diccionario)
    #documento=plantilla.render(contexto)
    return render(request, "familia/inicio.html")
    





