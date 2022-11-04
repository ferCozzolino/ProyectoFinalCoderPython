from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from .models import PlatoPrincipal
# Create your views here.


# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def platoPpal(request, combo, plato, guarnicion,precio):

    platoPpal = PlatoPrincipal(combo = combo, plato = plato, guarnicion = guarnicion, precio=precio)
    platoPpal.save()
    
    return HttpResponse(f"""
         <p> Combo: {platoPpal.combo} - Plato: {platoPpal.plato} - Guarnicion: {platoPpal.guarnicion} - Precio: ${platoPpal.precio} agregado! </p>
     """)




def bebida(request):
    
    return render(request,"bebidas.html")

def postre(request):
    return HttpResponse("Vista Postre")
    return render(request,"postres.html")