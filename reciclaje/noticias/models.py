from django.db import models
from django.utils import timezone


class Noticias(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="imagenes", null=True)
    texto = models.TextField()
    etiqueta = models.TextField(default="publico")
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

