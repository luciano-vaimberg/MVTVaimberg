from http.client import HTTPResponse
from django.shortcuts import render
from .models import Parientes
import datetime
from django.http import HttpResponse
from django.template import Context, Template

def papa(request):
    pariente1=Parientes(nombre="Pepe", parentesco ="Padre", edad = "65", fecha=datetime.datetime.today())
    pariente1.save()
    mensaje_papa=f"Mi nombre es <u><strong>{pariente1.nombre}</u></strong>, soy tu <strong>{pariente1.parentesco}</strong>, tengo <u>{pariente1.edad}</u> años <br><br> Fecha actual:<h3>{pariente1.fecha}</h3>"
    return HttpResponse(mensaje_papa)

def mama(request):
    pariente2=Parientes(nombre="Pepa", parentesco ="Madre", edad = "61", fecha=datetime.datetime.today())
    pariente2.save()
    mensaje_mama=f"Mi nombre es <u><strong>{pariente2.nombre}</strong></u>, soy tu <strong>{pariente2.parentesco}</strong>, tengo <u>{pariente2.edad}</u> años <br><br> Fecha actual:<h3>{pariente2.fecha}</h3>"
    return HttpResponse(mensaje_mama)    

def hijo(request):
    pariente3=Parientes(nombre="Pepito", parentesco ="Hijo", edad = "11", fecha=datetime.datetime.today())
    pariente3.save()
    mensaje_hijo=f"Mi nombre es <u><strong>{pariente3.nombre}</strong></u>, soy tu <strong>{pariente3.parentesco}</strong>, tengo <u>{pariente3.edad}</u> años <br><br> Fecha actual:<h3>{pariente3.fecha}</h3>"
    return HttpResponse(mensaje_hijo) 

def plantilla_html(request):

    fecha=datetime.datetime.today()
    diccionario={"fecha":fecha,}
    mihtml=open("C:/Users/Lucho/Desktop/MVT_PROYECTO/mvtFamilia/Plantillas/template1.html")
    plantilla=Template(mihtml.read())
    mihtml.close()
    contexto=Context(diccionario)
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
    





