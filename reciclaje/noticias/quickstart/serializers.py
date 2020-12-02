from django.contrib.auth.models import User, Group
from noticias.models import Noticias
from rest_framework import serializers
from django.utils import timezone

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class NoticiasSerializer(serializers.HyperlinkedModelSerializer):

    imagen = serializers.ImageField()
    fecha_publicacion = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = Noticias        
        fields = ('url', 'autor', 'titulo', 'imagen', 'texto', 'etiqueta', 'fecha_publicacion')