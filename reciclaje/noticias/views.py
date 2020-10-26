from django.shortcuts import render
from .models import Noticias
from django.utils import timezone

def inicio(request):
    return render(request, 'noticias/index.html', {})

def nosotros(request):
    return render(request, 'noticias/nosotros.html', {})

def lista_noticias(request):
    noticias = Noticias.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'noticias/noticias.html', {})

def proyectos(request):
    return render(request, 'noticias/proyectos.html', {})

def contacto(request):
    return render(request, 'noticias/contacto.html', {})