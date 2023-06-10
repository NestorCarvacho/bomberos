from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def lista_cuarteles(request):
    cuarteles = Cuartel.objects.all();

    for cuartel in cuarteles:
        cuartel.comuna_nombre = cuartel.comuna.nombre
    
    return render(request, 'lista_cuarteles.html', {'cuarteles' : cuarteles})

def form_mod_cuartel(request, id):
    cuartel = Cuartel.objects.filter(idCuartel=id).first()

    datos = {
        'form': CuartelForm(instance=cuartel)
    }

    if request.method == 'POST':
        formulario = CuartelForm(data=request.POST, instance=cuartel)
        if formulario.is_valid():
            formulario.save()

    return render(request, 'lista_cuarteles', datos)

def form_del_cuartel(request, id):
    cuarteles = Cuartel.objects.filter(idCuartel=id)
    
    for cuartel in cuarteles:
        cuartel.delete()
    
    return redirect(to="lista_cuarteles")

def form_cuartel(request):
    datos={
        'form': CuartelForm()

    }

    if request.method=='POST':
        formulario = CuartelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    
    return render(request,'form_cuartel.html',datos)

def lista_carros(request):
    carros = Carro.objects.all();

    for carro in carros:
        carro.cuartel.nombre = carro.cuartel.nombre
    
    return render(request, 'lista_carros.html', {'carros' : carros})

def form_mod_carro(request, id):
    carro = Carro.objects.filter(idCarro=id).first()

    datos = {
        'form': CarroForm(instance=carro)
    }

    if request.method == 'POST':
        formulario = CarroForm(data=request.POST, instance=carro)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_carros')

    return render(request, 'form_mod_carro.html', datos)



