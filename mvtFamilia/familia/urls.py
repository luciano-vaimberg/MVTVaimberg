from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name="inicio" ),
    path('papa/', papa, name="papa" ),
    path('mama/', mama, name="mama" ),
    path('hijo/', hijo, name="hijo" ),
]