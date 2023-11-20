from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pan
from .forms import PanForm
def inicio(request):
    return render(request, 'paginas/inicio.html')

def Init(request):
    return render(request, 'paginas/Init.html')

def Panes(request):
    Panes = Pan.objects.all()
    print(Panes)
    return render(request, 'Panes/index.html',{'Panes':Panes})

def crear(request):
    formulario = PanForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Panes')
    return render(request, 'Panes/crear.html',{'formulario':formulario})

def editar(request,id):
    pan=Pan.objects.get(id=id)
    formulario = PanForm(request.POST or None,request.FILES or None,instance=pan)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Panes')
    return render(request, 'Panes/editar.html',{'formulario':formulario,})
def eliminar(request,id):
    pan=Pan.objects.get(id=id)
    pan.delete()
    return redirect('Panes')
