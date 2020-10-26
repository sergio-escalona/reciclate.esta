from django.shortcuts import render

def inicio(request):
    return render(request, 'noticias/index.html', {})

def nosotros(request):
    return render(request, 'noticias/nosotros.html', {})

def lista_noticias(request):
    return render(request, 'noticias/noticias.html', {})

def proyectos(request):
    return render(request, 'noticias/proyectos.html', {})

def contacto(request):
    return render(request, 'noticias/contacto.html', {})