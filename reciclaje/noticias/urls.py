from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('noticias/', views.lista_noticias, name='lista_noticias'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('contacto/', views.contacto, name='contacto'),
    path('noticia/<int:pk>/', views.noticia_completa, name='noticia_completa'),
    path('noticia/nueva_noticia', views.nueva_noticia, name='nueva_noticia'),
    path('noticia/<int:pk>/editar/', views.editar_noticia, name='editar_noticia'),
    path('noticia/<int:pk>/eliminar', views.eliminar_noticia, name='eliminar_noticia'),
    path('cuenta/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)