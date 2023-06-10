from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="home"),
    path('lista_cuarteles',lista_cuarteles,name="lista_cuarteles"),
    path('form_mod_cuartel/<id>',form_mod_cuartel,name="form_mod_cuartel"),
    path('form_del_cuartel/<id>',form_del_cuartel, name="form_del_cuartel"),
    path('formulario/', formulario_reporte_fallas, name='formulario'),
]