from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pan,Empleado
from .forms import PanForm,EmpleadoForm
def inicio(request):
    return render(request, 'paginas/inicio.html')

def Init(request):
    return render(request, 'paginas/Init.html')

def Panes(request):
    Panes = Pan.objects.all()
    print(Panes)
    return render(request, 'Panes/index.html',{'Panes':Panes})

def crearP(request):
    formulario = PanForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Panes')
    return render(request, 'Panes/crear.html',{'formulario':formulario})

def editarP(request,id):
    pan=Pan.objects.get(id=id)
    formulario = PanForm(request.POST or None,request.FILES or None,instance=pan)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Panes')
    return render(request, 'Panes/editar.html',{'formulario':formulario,})
def eliminarP(request,id):
    pan=Pan.objects.get(id=id)
    pan.delete()
    return redirect('Panes')
def Empleados(request):
    Empleados = Empleado.objects.all()
    print(Empleados)
    return render(request, 'Empleados/index.html',{'Empleados':Empleados})    
def crearE(request):
    formulario = EmpleadoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Empleados')
    return render(request, 'Empleados/crear.html',{'formulario':formulario})
def editarE(request,id):
    empleado=Empleado.objects.get(id=id)
    formulario = EmpleadoForm(request.POST or None,request.FILES or None,instance=empleado)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Empleados')
    return render(request, 'Empleados/editar.html',{'formulario':formulario,})
def eliminarE(request,id):   
    empleado=Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('Empleados')
