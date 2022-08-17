
from django import forms
from django.forms import ModelForm, ClearableFileInput
from .models import Clientes, ComentarioUsuario, Archivos

class CustomClearableFieldInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields = ('nombre', 'mensaje', 'email', 'archivo')
        widgets = {
            'archivo': CustomClearableFieldInput
        }

class ComentarioUserForm(forms.ModelForm):
    class Meta:
        model = ComentarioUsuario
        fields = ['nombre','email', 'mensaje']

class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre_c','apellido_p','apellido_m','correo_c','telefono_c','tour_c','mensaje_c']


