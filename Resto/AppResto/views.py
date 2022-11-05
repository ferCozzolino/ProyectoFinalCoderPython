from ast import Return
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import PlatoPrincipal, Bebida, Postre
from .forms import BebidaFormulario, PostreFormulario, PlatoPpalFormulario
# Create your views here.


# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def platoPpal(request):


    return render(request,"platos.html")

def bebida(request):
    lista = Bebida.objects.all()
    return render(request, "bebidas.html", {"lista_bebidas": lista})
    

def postre(request):

    return render(request,"postres.html")

def lista_bebida(request):
    lista = Bebida.objects.all()
    return render(request, "bebidas.html", {"lista_bebidas": lista})

# FORMULARIOS

def bebidaFormulario(request):

    print('method: ', request.method)
    print('post: ', request.POST)


    if request.method =='POST':
        mi_formulario_de_bebida = BebidaFormulario(request.POST)
        print (mi_formulario_de_bebida)
        if mi_formulario_de_bebida.is_valid():
            data = mi_formulario_de_bebida.cleaned_data
            bebida = Bebida(codBebida=data['codBebida'], bebida=data['bebida'], precio=data['precio'])
            bebida.save()

        return redirect('bebidaFormulario')
    else:
        mi_formulario_de_bebida = BebidaFormulario()

    return render(request, "bebidaFormulario.html", {'mi_formulario_de_bebida': mi_formulario_de_bebida})



def postreFormulario(request):

    print('method: ', request.method)
    print('post: ', request.POST)


    if request.method =='POST':
        mi_formulario_de_postre = PostreFormulario(request.POST)
        print (mi_formulario_de_postre)
        if mi_formulario_de_postre.is_valid():
            data = mi_formulario_de_postre.cleaned_data
            postre = Postre(codPostre=data['codPostre'], postre=data['postre'], precio=data['precio'])
            postre.save()

        return redirect('postreFormulario')
    else:
        mi_formulario_de_postre = PostreFormulario()

    return render(request, "postreFormulario.html", {'mi_formulario_de_postre': mi_formulario_de_postre})

def platoPpalFormulario(request):

    print('method: ', request.method)
    print('post: ', request.POST)


    if request.method =='POST':
        mi_formulario_de_platoPpal = PlatoPpalFormulario(request.POST)
        print (mi_formulario_de_platoPpal)
        if mi_formulario_de_platoPpal.is_valid():
            data = mi_formulario_de_platoPpal.cleaned_data
            platoPpal = PlatoPrincipal(combo=data['combo'], plato=data['plato'], guarnicion=data['guarnicion'], precio=data['precio'])
            platoPpal.save()

        return redirect('platoPpalFormulario')
    else:
        mi_formulario_de_platoPpal = PlatoPpalFormulario()

    return render(request, "platoPpalFormulario.html", {'mi_formulario_de_platoPpal': mi_formulario_de_platoPpal})   

# Busquedas

def busqueda_bebida(request):
    return render(request, 'busqueda_bebida.html')

def buscar_bebida(request):
    bebida_buscada = request.GET['bebida']
    precioBebida = Bebida.objects.get(bebida = bebida_buscada)
    
    

    return render(request, 'resultadoBusquedaBebida.html', {'precioBebida:': precioBebida, 'bebida': bebida_buscada})

def busqueda_postre(request):
    return render(request, "busqueda_postre.html")

def buscar_postre(request):
    postre_buscado = request.GET['postre']
    precioPostre = Postre.objects.get(postre = postre_buscado)

    return render(request, 'resultadoBusquedaPostre.html', {'precio': precioPostre, 'postre':postre_buscado})