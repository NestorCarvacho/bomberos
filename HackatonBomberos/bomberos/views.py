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

def form_del_carro(request, id):
    carros = Carro.objects.filter(idCarro=id)
    
    for carro in carros:
        carro.delete()
    
    return redirect(to="lista_carros")

def form_carro(request):
    datos={
        'form': FormularioCarro()
    }

    if request.method=='POST':
        formulario = FormularioCarro(request.POST)
        if formulario.is_valid():
            formulario.save()
    
    return render(request,'form_carros.html',datos)

def lista_cargos(request):
    cargos = Cargo.objects.all();
    
    return render(request, 'lista_carros.html', {'cargos' : cargos})

def formulario_reporte_fallas(request):
    if request.method == 'POST':
        form = ReporteFallaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Realizar acciones adicionales si es necesario
    else:
        form = ReporteFallaForm()
    
    context = {'form': form}
    return render(request, 'form_reporte_fallas.html', context)

def donaciones(request):
    form = DonacionForm()

    if request.method == 'POST':
        form = DonacionForm(request.POST)
        if form.is_valid():
            # Aquí puedes procesar y almacenar los datos de la donación en la base de datos
            # y realizar cualquier otra acción necesaria
            return redirect('agradecimiento')

    return render(request, 'donaciones.html', {'form': form})

def agradecimiento(request):
    return render(request, 'agradecimiento.html')


def confirmar_donacion(request):
    return render(request, 'confirmar_donacion.html')