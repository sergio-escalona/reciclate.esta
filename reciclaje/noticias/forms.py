from django import forms

from .models import Noticias, Contacto

class FormularioNoticia(forms.ModelForm):

    class Meta:
        model = Noticias
        fields = ('titulo', 'imagen', 'texto', 'etiqueta',)

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre','correo','telefono','mensaje','motivo','respuesta')