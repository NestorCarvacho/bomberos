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

class BomberoModificar(ModelForm):
    rut = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    dv = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Bombero
        fields = ['rut','dv', 'nombre', 'apPaterno', 'apMaterno', 'edad', 'telefono', 'direccion', 'cargo']

        

class ReporteFallaForm(forms.ModelForm):
    hidrante = forms.ModelChoiceField(queryset=Hidrante.objects.all(), empty_label=None, widget=forms.Select)
    estado_hidrante = forms.ChoiceField(choices=ESTADOS_HIDRANTE, widget=forms.Select)

    class Meta:
        model = ReporteFalla
        fields = [ 'rut', 'nombre', 'apellido', 'correo', 'telefono', 'hidrante', 'estado_hidrante', 'comentario', 'foto']

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['nombre', 'email', 'monto', 'metodo_pago', 'cuartel']


class FormularioHidrante(forms.ModelForm):
    
    class Meta:
        model = Hidrante
        fields = ['idHidrante','direccion','estado']