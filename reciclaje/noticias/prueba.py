from reciclaje.noticias.models import Contacto, Noticias
from django.utils import timezone
from django.http import request

def listar(eti):
    noticias = Noticias.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion').filter(etiqueta=eti).count()
    return noticias

def contacto(nombre, correo, fono, mensaje, motivo, respuesta):
    contacto = Contacto()
    contacto.nombre = request.POST.get(nombre)
    contacto.correo = request.POST.get(correo)
    contacto.telefono = request.POST.get(fono)
    contacto.mensaje = request.POST.get(mensaje)
    contacto.motivo = request.POST.get(motivo)
    contacto.respuesta = request.POST.get(respuesta)
    if contacto.save():
        return True
    else:
        return False