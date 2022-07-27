from django.shortcuts import redirect, render

from complejos.forms import ParquesForm, EstadiosForm
from complejos.models import Estadios, Parques


# Create your views here.

def index(request):
    return render(request, 'index.html')

# Parques

def crearParque(request):
    
    if request.method == 'POST':
        form = ParquesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complejos:listar-parque')
    else:
        form = ParquesForm()
    diccionario = {'formulario': form}

    return render(request, 'crearParques.html', diccionario) 

    
 # Listar   
    
def listarParque(request):
    parques = Parques.objects.all().order_by('id')
    informacion = {'parques': parques}
    return render(request, 'listarParques.html', informacion)

# Editar 

def editarParque(request, id_parque):
    parques = Parques.objects.all().get(id=id_parque)
    if request.method == 'GET':
        form = ParquesForm(instance=parques)
    else:
        form = ParquesForm(request.POST, instance=parques)
        if form.is_valid():
            form.save()
            return redirect('complejos:listar-parque')
    diccionario = {'formulario': form}
    return render(request, 'crearParques.html', diccionario)
        
# Eliminar

def eliminarParques(request, id_parque):
    parques = Parques.objects.all().get(id=id_parque)
    if request.method == 'POST':
        parques.delete()
        return redirect('complejos:listar-parque')
    diccionario = {'parques': parques}
    return render(request, 'eliminarParque.html', diccionario)
    
    
    


 
# Estadios
    
def crearEstadios(request):
    
    if request.method == 'POST':
        form = EstadiosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complejos:listar-estadios')
    else:
        form = EstadiosForm()
    diccionario = {'formulario': form}

    return render(request, 'crearEstadios.html', diccionario) 
    

# Listar
    
def listarEstadios(request): 
    estadios = Estadios.objects.all().order_by('id')
    informacion = {'estadios': estadios}
    return render(request, 'listarEstadios.html', informacion)   



# Editar 

def editarEstadios(request, id_estadios):
    estadios = Estadios.objects.all().get(id=id_estadios)
    if request.method == 'GET':
        form = EstadiosForm(instance=estadios)
    else:
        form =EstadiosForm(request.POST, instance=estadios)
        if form.is_valid():
            form.save()
            return redirect('complejos:listar-estadios')
    diccionario = {'formulario': form}
    return render(request, 'crearEstadios.html', diccionario)
    


# Eliminar

def eliminarEstadios(request, id_estadios):
    estadios = Estadios.objects.all().get(id=id_estadios)
    if request.method == 'POST':
        estadios.delete()
        return redirect('complejos:listar-estadios')
    diccionario = {'estadios': estadios}
    return render(request, 'eliminarEstadios.html', diccionario)

