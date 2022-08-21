from http.client import HTTPResponse
from django.shortcuts import render
from .models import Parientes
import datetime
from django.http import HttpResponse
from django.template import Context, Template

def papa(request):
    pariente1=Parientes(nombre="Pepe", parentesco ="Padre", edad = "65", fecha=datetime.datetime.today())
    pariente1.save()
    mensaje_papa=f"Mi nombre es {pariente1.nombre}, soy tu {pariente1.parentesco}, tengo {pariente1.edad} años y hoy es {pariente1.fecha}"
    return HttpResponse(mensaje_papa)

def mama(request):
    pariente2=Parientes(nombre="Pepa", parentesco ="Madre", edad = "61", fecha=datetime.datetime.today())
    pariente2.save()
    mensaje_mama=f"Mi nombre es {pariente2.nombre}, soy tu {pariente2.parentesco}, tengo {pariente2.edad} años y hoy es {pariente2.fecha}"
    return HttpResponse(mensaje_mama)    

def hijo(request):
    pariente3=Parientes(nombre="Pepito", parentesco ="Hijo", edad = "11", fecha=datetime.datetime.today())
    pariente3.save()
    mensaje_hijo=f"Mi nombre es {pariente3.nombre}, soy tu {pariente3.parentesco}, tengo {pariente3.edad} años y hoy es {pariente3.fecha}"
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
    


   


