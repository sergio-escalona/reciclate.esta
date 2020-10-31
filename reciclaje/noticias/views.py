from django.shortcuts import get_object_or_404, render
from .models import Noticias, Contacto
from django.utils import timezone
from .forms import FormularioNoticia, FormularioContacto
from django.shortcuts import redirect

def inicio(request):
    return render(request, 'noticias/index.html', {})

def nosotros(request):
    return render(request, 'noticias/nosotros.html', {})

def lista_noticias(request):
    usuario = request.user
    if usuario.has_perm('noticias.editor'):
        noticias = Noticias.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    elif  usuario.has_perm('noticias.lector'):
        noticias = Noticias.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion').filter(etiqueta=0)
    else:
        noticias = Noticias.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion').filter(etiqueta=3)
    return render(request, 'noticias/noticias.html', {'noticias': noticias})

def proyectos(request):
    return render(request, 'noticias/proyectos.html', {})

def contacto(request):
    data = {
        'formCont': FormularioContacto()
    }

    if request.method == "POST":
        contacto = FormularioContacto(data=request.POST)
        if contacto.is_valid():
            contacto.save()
            data["mensaje"] = "Mensaje enviado"
        
        else:
            data["formCont"] = contacto
            data["mensaje"] = "Error al enviar mensaje"
    return render(request, 'noticias/contacto.html', data)

def fomulario_contacto(request):
    if request.method == "POST":
        contacto = Contacto()
        contacto.nombre = request.POST.get('nombre')
        contacto.correo = request.POST.get('correo')
        contacto.telefono = request.POST.get('fono')
        contacto.mensaje = request.POST.get('mensaje')
        contacto.motivo = request.POST.get('motivo')
        contacto.respuesta = request.POST.get('respuesta')
        contacto.save()
        return render(request, 'noticias/contacto.html', {})
    
    else:
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

def eliminar_noticia(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    noticia.delete()
    return redirect(to='lista_noticias')