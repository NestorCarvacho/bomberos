from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="home"),
    path('index',index, name="home"),
    path('lista_cuarteles',lista_cuarteles,name="lista_cuarteles"),
    path('form_mod_cuartel/<id>',form_mod_cuartel,name="form_mod_cuartel"),
    path('form_del_cuartel/<id>',form_del_cuartel, name="form_del_cuartel"),
    path('form_cuartel',form_cuartel,name="form_cuartel"),
    path('lista_carros',lista_carros,name="lista_carros"),
    path('form_mod_carro/<id>',form_mod_carro,name="form_mod_carro"),
    path('form_del_carro/<id>',form_del_carro,name="form_del_carro"),
    path('form_carros',form_carro,name="form_carros"),
    path('lista_cargos',lista_cargos,name="lista_cargos"),
    path('nuestros_funcionarios', nuestros_funcionarios, name='nuestros_funcionarios'),
    path('nuestra_historia', nuestra_historia, name='nuestra_historia'),
    path('contacto', contacto, name='contacto'),
]