from django.shortcuts import get_object_or_404, render
from .models import Noticias
from django.utils import timezone
from .forms import FormularioNoticia
from django.shortcuts import redirect

def inicio(request):
    return render(request, 'noticias/index.html', {})

def nosotros(request):
    return render(request, 'noticias/nosotros.html', {})

def lista_noticias(request):
    noticias = Noticias.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'noticias/noticias.html', {'noticias': noticias})

def proyectos(request):
    return render(request, 'noticias/proyectos.html', {})

def contacto(request):
    return render(request, 'noticias/contacto.html', {})

def noticia_completa(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    return render(request, 'noticias/noticia_completa.html', {'noticia': noticia})

def nueva_noticia(request):
    if request.method == "POST":
        formNoti = FormularioNoticia(data=request.POST, files=request.FILES)
        if formNoti.is_valid():
            noticia = formNoti.save(commit=False)
            noticia.autor = request.user
            noticia.fecha_publicacion = timezone.now()
            noticia.save()
            return redirect('noticia_completa', pk=noticia.pk)
        else:
            return render(request, 'noticias/editar_noticia.html', {'formNoti': formNoti})
    else:
        formNoti = FormularioNoticia()
        return render(request, 'noticias/editar_noticia.html', {'formNoti': formNoti})

def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    if request.method == "POST":
        formNoti = FormularioNoticia(request.POST, request.FILES, instance=noticia)
        if formNoti.is_valid():
            noticia = formNoti.save(commit=False)
            noticia.author = request.user
            noticia.published_date = timezone.now()
            noticia.save()
            return redirect('noticia_completa', pk=noticia.pk)
    else:
        formNoti = FormularioNoticia(instance=noticia)
        return render(request, 'noticias/editar_noticia.html', {'formNoti': formNoti})
