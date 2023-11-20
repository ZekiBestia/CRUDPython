from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Init/', views.Init, name='Init'),
    path('Panes/', views.Panes, name='Panes'),
    path('Panes/crear', views.crear, name='crear'),
    path('Panes/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('Panes/editar/<int:id>', views.editar, name='editar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)