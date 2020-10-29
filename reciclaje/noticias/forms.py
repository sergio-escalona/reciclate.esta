from django import forms

from .models import Noticias, Contacto
from django.db.models.functions import Length
from django.forms import ValidationError
import re

class FormularioNoticia(forms.ModelForm):

    class Meta:
        model = Noticias
        fields = ('titulo', 'imagen', 'texto', 'etiqueta',)

class FormularioContacto(forms.ModelForm):

    error_css_class = 'error'

    #validadores
    nombre = forms.CharField(required=False)
    correo = forms.EmailField(required=False)
    telefono = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(FormularioContacto, self).__init__(*args, **kwargs)
        self.fields["mensaje"].required = False
        self.fields["motivo"].required = False

    def clean_nombre(self):
        super(FormularioContacto, self).clean()
        nombre = self.cleaned_data['nombre']
        
        if len(nombre)<3:
            raise ValidationError("Nombre debe tener al menos 3 carácteres")

        return nombre

    def clean_correo(self):
        super(FormularioContacto, self).clean()
        correo = self.cleaned_data['correo']
        
        if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', correo) != None or len(correo)<8:
            raise ValidationError("Ingrese un correo válido")
        
        return correo

    def clean_telefono(self):
        super(FormularioContacto, self).clean()
        telefono = self.cleaned_data['telefono']
        
        if telefono is None or telefono<100000:
            raise ValidationError("Teléfono debe tener al menos 6 números")

        return telefono

    def clean_mensaje(self):
        super(FormularioContacto, self).clean()
        mensaje = self.cleaned_data['mensaje']
        
        if len(mensaje)<3:
            raise ValidationError("Mensaje debe tener al menos 10 carácteres")

        return mensaje

    def clean_motivo(self):
        super(FormularioContacto, self).clean()
        motivo = self.cleaned_data['motivo']
        
        if motivo=="":
            raise ValidationError("Elija una opción")

        return motivo

    class Meta:
        model = Contacto
        fields = ('nombre','correo','telefono','mensaje','motivo','respuesta',)

    
    
    
    
    
        
