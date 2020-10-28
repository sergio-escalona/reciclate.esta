from django import forms

from .models import Noticias

class FormularioNoticia(forms.ModelForm):

    class Meta:
        model = Noticias
        fields = ('titulo', 'imagen', 'texto', 'etiqueta',)
