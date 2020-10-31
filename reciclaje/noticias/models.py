from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

etiquetas = [
    [0, "Publico"],
    [1, "Privado"],
]

class Noticias(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="imagenes", null=True)
    texto = models.TextField()
    etiqueta = models.IntegerField(choices=etiquetas)
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
    class Meta:
        permissions = (
            ('editor',_('Es editor')),
            ('lector',_('Es lector')),
        )


motivos = [
    [0, "Sujerencia"],
    [1, "Queja"],
    [2, "Trabajar con nosotros"],
    [3, "Donación"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=75)
    correo = models.EmailField()
    telefono = models.IntegerField(default=None,blank=True, null=True)
    mensaje = models.TextField()
    motivo = models.IntegerField(choices=motivos)
    respuesta = models.BooleanField()

    def __str__(self):
        return self.nombre