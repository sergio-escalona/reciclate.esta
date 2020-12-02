from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers
from noticias.quickstart import view

router = routers.DefaultRouter()
router.register(r'users', view.UserViewSet)
router.register(r'groups', view.GroupViewSet)
router.register(r'api_noticias', view.NoticiasViewSet)


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
    path('cuenta/', include('django.contrib.auth.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', include('pwa.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)