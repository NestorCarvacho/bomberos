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

    return render(request, 'form_mod_cuartel.html', datos)

def form_del_cuartel(request, id):
    cuarteles = Cuartel.objects.filter(idCuartel=id)
    
    for cuartel in cuarteles:
        cuartel.delete()
    
    return redirect(to="lista_cuarteles")