from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Init/', views.Init, name='Init'),
    path('Panes/', views.Panes, name='Panes'),
    path('Panes/crear', views.crearP, name='crearP'),
    path('Panes/editar', views.editarP, name='editarP'),
    path('eliminar/<int:id>', views.eliminarP, name='eliminarP'),
    path('Panes/editar/<int:id>', views.editarP, name='editarP'),
    path('Empleados/', views.Empleados, name='Empleados'),
    path('Empleados/crear', views.crearE, name='crearE'),
    path('Empleados/editar', views.editarE, name='editarE'),
    path('Empleados/editar/<int:id>', views.editarE, name='editarE'),
    path('eliminar/<int:id>', views.eliminarE, name='eliminarE'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)