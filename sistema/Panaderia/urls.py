from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Init/', views.Init, name='Init'),
    path('Panes/', views.Panes, name='Panes'),
    path('Panes/crear', views.crear_pan, name='crearPanes'),
    path('Panes/editar', views.editar_pan, name='editarPanes'),
    path('eliminar/<int:id>', views.eliminar_pan, name='eliminarPanes'),
    path('Panes/editar/<int:id>', views.editar_pan, name='editarPanes'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)