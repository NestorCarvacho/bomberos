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
    
    return render(request, 'lista_cargos.html', {'cargos' : cargos})

def form_mod_cargo(request, id):
    cargo = Cargo.objects.filter(idCargo=id).first()

    datos = {
        'form': CargoForm(instance=cargo)
    }

    if request.method == 'POST':
        formulario = CargoForm(data=request.POST, instance=cargo)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_cargos')

    return render(request, 'form_mod_cargo.html', datos)

def form_del_cargo(request, id):
    cargo = Cargo.objects.filter(idCargo=id)
    
    for cargo in cargo:
        cargo.delete()
    
    return redirect(to="lista_cargos")

def form_cargos(request):
    datos={
        'form': CargoForm()
    }

    if request.method=='POST':
        formulario = CargoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    
    return render(request,'form_cargos.html',datos)

def lista_bomberos(request):
    bomberos = Bombero.objects.all();

    for bombero in bomberos:
        bombero.cuartel.nombre = bombero.cuartel.nombre
    
    return render(request, 'lista_bomberos.html', {'bomberos' : bomberos})

def form_mod_bombero(request, id):
    bombero = Bombero.objects.filter(idBombero=id).first()

    datos = {
        'form': BomberoModificar(instance=bombero)
    }

    if request.method == 'POST':
        formulario = BomberoModificar(data=request.POST, instance=bombero)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_bomberos')

    return render(request, 'form_mod_bombero.html', datos)

def form_del_bombero(request, id):
    bomberos = Bombero.objects.filter(idBombero=id)

    for bombero in bomberos:
        bombero.delete()

    return redirect('lista_bomberos')

def form_bombero(request):
    datos={
        'form': BomberoForm()
    }

    if request.method=='POST':
        formulario = BomberoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    
    return render(request,'form_bombero.html',datos)

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
def nuestros_funcionarios(request):
    bomberos = Bombero.objects.all()  # Obtener todos los objetos de la tabla Bombero

    context = {
        'bomberos': bomberos  # Pasar los bomberos como contexto a la plantilla HTML
    }

    return render(request, 'nuestros_funcionarios.html', context)

def nuestra_historia(request):
    return render(request,'nuestra_historia.html')
