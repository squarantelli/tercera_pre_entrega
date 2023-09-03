from django.http import HttpResponse
from django.shortcuts import render
from EstampasVoodoo.models import *
from EstampasVoodoo.forms import *

# Create your views here.

def inicio(request):
    return render(request, "EstampasVoodoo/inicio.html")

def clientes(request):
    return render(request, "EstampasVoodoo/clientes.html")

def setCliente(request):
    if request.method == 'POST':
        miFormulario = formSetCliente(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            cliente = Cliente(nombre=data["nombre"],apellido=data["apellido"],telefono=data["telefono"], email=data["email"])    
            cliente.save()
            return render(request,"EstampasVoodoo/inicio.html")    
    else:
        miFormulario = formSetCliente()
    return render(request, "EstampasVoodoo/setCliente.html", {"miFormulario":miFormulario})

def getCliente(request):
    return render(request, "EstampasVoodoo/getCliente.html")

def searchCliente(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        clientes = Cliente.objects.filter(nombre = nombre)
        return render(request, "EstampasVoodoo/getCliente.html", {"clientes":clientes})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

def remeras(request):
    return render(request, "EstampasVoodoo/remeras.html")

def setRemera(request):
    if request.method == 'POST':
        miFormulario = formSetRemera(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            remera = Remera(codigo=data["codigo"],nombre=data["nombre"],talle=data["talle"])    
            remera.save()
            return render(request,"EstampasVoodoo/inicio.html")    
    else:
        miFormulario = formSetRemera()
    return render(request, "EstampasVoodoo/setRemera.html", {"miFormulario":miFormulario})

def getRemera(request):
    return render(request, "EstampasVoodoo/getRemera.html")

def searchRemera(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        remeras = Remera.objects.filter(nombre = nombre)
        return render(request, "EstampasVoodoo/getRemera.html", {"remeras":remeras})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)

def tazas(request):
    return render(request, "EstampasVoodoo/tazas.html")

def setTaza(request):
    if request.method == 'POST':
        miFormulario = formSetTaza(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            taza = Taza(codigo=data["codigo"],nombre=data["nombre"])    
            taza.save()
            return render(request,"EstampasVoodoo/inicio.html")    
    else:
        miFormulario = formSetTaza()
    return render(request, "EstampasVoodoo/setTaza.html", {"miFormulario":miFormulario})

def getTaza(request):
    return render(request, "EstampasVoodoo/getTaza.html")

def searchTaza(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        tazas = Taza.objects.filter(nombre = nombre)
        return render(request, "EstampasVoodoo/getTaza.html", {"tazas":tazas})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)