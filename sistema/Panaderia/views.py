from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pan,Empleado
from .forms import PanForm,EmpleadoForm
from django.shortcuts import get_object_or_404
def inicio(request):
    return render(request, 'paginas/inicio.html')

def Init(request):
    return render(request, 'paginas/Init.html')

def Panes(request):
    # esta recupera todos los datos de la base de datos
    Panes = Pan.objects.all()
    return render(request, 'Panes/index.html',{'Panes':Panes})
def crearP(request):
    formulario = PanForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Panes')
    # renderizar la plantilla 'crear.html' junto con el formulario
    return render(request, 'Panes/crear.html',{'formulario':formulario})

def editarP(request,id):
    pan=Pan.objects.get(id=id)
    formulario = PanForm(request.POST or None,request.FILES or None,instance=pan)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Panes')
    return render(request, 'Panes/editar.html',{'formulario':formulario,})
def eliminarP(request,id):
    pan = get_object_or_404(Pan, id=id)
    pan.delete()
    return redirect('Panes')
def Empleados(request):
    # esta recupera todos los datos de la tabla Empleadopoy
    Empleados = Empleado.objects.all()
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
