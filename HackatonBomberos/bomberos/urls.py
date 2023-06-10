from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="home"),
    path('lista_cuarteles',lista_cuarteles,name="lista_cuarteles"),
    path('form_mod_cuartel/<id>',form_mod_cuartel,name="form_mod_cuartel"),
    path('form_del_cuartel/<id>',form_del_cuartel, name="form_del_cuartel"),
    path('form_cuartel',form_cuartel,name="form_cuartel"),
    path('lista_carros',lista_carros,name="lista_carros"),
    path('form_mod_carro/<id>',form_mod_carro,name="form_mod_carro"),
]