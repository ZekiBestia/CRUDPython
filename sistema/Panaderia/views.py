from django.shortcuts import render, redirect
from .models import Pan
from .forms import PanForm
from django.shortcuts import render, redirect, get_object_or_404


def inicio(request):
    return render(request, 'paginas/inicio.html')

def Init(request):
    return render(request, 'paginas/Init.html')

def Panes(request):
    panes = Pan.objects.all()
    return render(request, 'Panes/index.html', {'panes': panes})

def crear_pan(request):
    formulario = PanForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('Panes')
    return render(request, 'Panes/crear.html', {'formulario': formulario})

def editar_pan(request,id):
    pan = Pan.objects.get(id=id)
    pan = get_object_or_404(Pan, id=id)
    formulario = PanForm(request.POST or None, request.FILES or None, instance=pan)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('Panes')
    return render(request, 'Panes/editar.html', {'formulario': formulario})

def eliminar_pan(request,id):
    pan = Pan.objects.get(id=id)
    pan.delete()
    return redirect('Panes')
