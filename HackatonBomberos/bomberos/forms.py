from django import forms
from django.forms import ModelForm
from .models import *

class ComunaForm(ModelForm):
    class Meta:
        model = Comuna
        fields = ['nombre']
        
class CuartelForm(ModelForm):
    class Meta:
        model = Cuartel
        fields = ['nombre','direccion','comuna']
        
class CarroForm(forms.ModelForm):
    patente = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Carro
        fields = ['patente', 'marca', 'modelo', 'anno', 'capacidadPersonas', 'capacidadLitros', 'cuartel']
        
class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre']
        
class BomberoForm(ModelForm):
    class Meta:
        model = Bombero
        fields = ['rut','dv', 'nombre', 'apPaterno', 'apMaterno', 'edad', 'telefono', 'direccion', 'cargo']
        
class TipoEmergenciaForm(ModelForm):
    class Meta:
        model = TipoEmergencia
        fields = ['nombre']
        
class EmergenciaForm(ModelForm):
    class Meta:
        model = Emergencia
        fields = ['tipo', 'descripcion', 'fechaInicio']

class FormularioCarro(forms.ModelForm):
    
    class Meta:
        model = Carro
        fields = ['patente', 'marca', 'modelo', 'anno', 'capacidadPersonas', 'capacidadLitros', 'cuartel']

        

class ReporteFallaForm(forms.ModelForm):

    class Meta:
        model = ReporteFalla
        fields = ['rut', 'nombre', 'apellido', 'correo',
                  'telefono', 'direccion', 'comentario', 'foto']
        widgets = {
            'rut': forms.TextInput(attrs={'pattern': '\d{1,2}\.\d{3}\.\d{3}-[0-9kK]{1}', 'title': 'Ingrese un RUT válido (Ejemplo: 12.345.678-9)'}),
            'comentario': forms.Textarea(attrs={'rows': 4}),
        }

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['nombre', 'email', 'monto', 'metodo_pago', 'cuartel']
