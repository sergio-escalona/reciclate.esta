from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('noticias/', views.lista_noticias, name='lista_noticias'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('contacto/', views.contacto, name='contacto'),
]
