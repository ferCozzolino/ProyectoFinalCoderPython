from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required   
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *  


# Create your views here.
#----------------------------------------------------------------------------------------------------------

def inicio(request):
    
    #avatar = Avatar.objects.get(user=request.user)
    return render(request, "inicio.html")
    #return render(request, "inicio.html", {"url": avatar.imagen.url})

def curso(request, camada, nombre):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado! </p>
    """)

def bebida(request, bebida, precio):

    bebida = Bebida(bebida=bebida, precio=precio)
    bebida.save()

    return HttpResponse(f"""
        <p>Bebida: {bebida.bebida} - Precio: {bebida.precio} agregado! </p>
    """)


def postre(request, postre, precio):

    postre = Postre(postre=postre, precio=precio)
    postre.save()

    return HttpResponse(f"""
        <p>Postre: {postre.postre} - Precio: {postre.precio} agregado! </p>
    """)

def plato(request, plato, guarnicion, precio):

    plato = Plato(plato=plato, guarnicion=guarnicion, precio=precio)
    plato.save()

    return HttpResponse(f"""
        <p>Plato: {plato.plato} - Guarnicion: {plato.guarnicion} - Precio: {plato.precio} agregado! </p>
    """)


# Secciones
#----------------------------------------------------------------------------------------------------------


def bebidas(request):

    lista = Bebida.objects.all()
    return render(request, "bebidas.html", {"lista_bebida": lista})

def platos(request):
    
    #return render(request, "platos.html")
    lista = Plato.objects.all()
    return render(request, "platos.html", {"lista_plato": lista})

@login_required
def postres(request):

    lista = Postre.objects.all()
    return render(request, "postres.html", {"lista_postre": lista})
    #return render(request, "postres.html")

# Listados
#----------------------------------------------------------------------------------------------------------
def lista_curso(request):

    lista = Curso.objects.all()

    return render(request, "lista_cursos.html", {"lista_cursos": lista})

def lista_bebida(request):

    lista = Bebida.objects.all()

    return render(request, "lista_bebida.html", {"lista_bebida": lista})

def lista_postre(request):

    lista = Postre.objects.all()

    return render(request, "lista_postre.html", {"lista_postre": lista})

def lista_plato(request):

    lista = Plato.objects.all()

    return render(request, "lista_plato.html", {"lista_plato": lista})



# Formularios
#----------------------------------------------------------------------------------------------------------

def bebidaFormulario(request):

    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
        
        mi_formulario_de_bebida = BebidaFormulario(request.POST)
        print(mi_formulario_de_bebida)
        if  mi_formulario_de_bebida.is_valid():
            data = mi_formulario_de_bebida.cleaned_data
            bebida = Bebida(bebida=data['bebida'], precio=data['precio'])
            bebida.save()
            return redirect ('Bebidas')
    else:
            mi_formulario_de_bebida = BebidaFormulario()   
        
    return render(request, "bebidaFormulario.html", {'pepe': mi_formulario_de_bebida})


# Busquedas


def busqueda_bebida(request):
    return render(request, 'busqueda_bebida.html')

def buscar_bebida(request):
    if request.GET["bebida"]:

        bebida_buscada = request.GET['bebida']
        bebidas = Bebida.objects.get(bebida = bebida_buscada) 

    return render(request, 'resultadoBusquedaBebida.html', {'bebidas': bebidas, 'bebida': bebida_buscada })

def busqueda_camada(request):
    return render(request, 'busqueda_camada.html')

def buscar(request):
    camada_buscada = request.GET['camada']
    curso = Curso.objects.get(camada = camada_buscada)

    return render(request, 'resultadoBusqueda.html',{'curso': curso, 'camada': camada_buscada})


# CRUD
#-----------------------------------------------------------------------------------------------------

# CREATE

def crea_bebida(request):

    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
        
        mi_formulario_de_bebida = BebidaFormulario(request.POST)
        print(mi_formulario_de_bebida)
        if  mi_formulario_de_bebida.is_valid():
            data = mi_formulario_de_bebida.cleaned_data
            bebida = Bebida(bebida=data['bebida'], precio=data['precio'])
            bebida.save()
            return redirect ('Bebidas')
    else:
            mi_formulario_de_bebida = BebidaFormulario()           
            return render(request, "bebidaFormulario.html", {'pepe': mi_formulario_de_bebida})


# READ

def leerBebidas(request):
    bebidas = Bebida.objects.all()
    return render(request, "leerBebidas.html", {"bebidas": bebidas})


# UPDATE

def editar_bebida(request, id):

    print('method: ', request.method)
    print('post: ', request.POST)

    bebida = Bebida.objects.get(id=id)
    if request.method == 'POST':
        
        mi_formulario_de_bebida = BebidaFormulario(request.POST)
        print(mi_formulario_de_bebida)
        if  mi_formulario_de_bebida.is_valid():
            data = mi_formulario_de_bebida.cleaned_data
            bebida.bebida = data["bebida"]
            bebida.precio = data["precio"]
            bebida.save()
            return redirect ('Bebidas')
    else:
            mi_formulario_de_bebida = BebidaFormulario(initial={
                "bebida": bebida.bebida,
                "precio": bebida.precio
            })           
            return render(request, "editar_bebida.html", {'pepe': mi_formulario_de_bebida, "id": bebida.id})
    
# DELETE

def eliminar_bebida(request, id):

    if request.method == 'POST':
        bebida = Bebida.objects.get(id=id)
        bebida.delete()
        bebidas = Bebida.objects.all()
        return render(request, "leerBebidas.html", {"bebidas": bebidas})


# Login

def loginView(request):

    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
        
        mi_formulario = AuthenticationForm(request, data=request.POST)
        print(mi_formulario)
        if  mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            
            if user:
                login(request, user)
                return render(request, "inicio.html", {'mensaje': f'Bienvenido {usuario} !'})
            else:
                return render(request, "inicio.html", {'mensaje': f'Error, datos incorrectos'})

        return render(request, "inicio.html", {'mensaje': f'Error, formulario invalido'})
    else:
            mi_formulario = AuthenticationForm()         
            return render(request, "login.html", {'pepe': mi_formulario})


def register(request):
    
    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
        
        mi_formulario = UserEditForm(request.POST)
        
        if  mi_formulario.is_valid():
            username = mi_formulario.cleaned_data["username"]
            mi_formulario.save()

            return render(request, "inicio.html", {'mensaje': f'Usuario: {username} creado correctamente!'})
        else:
            return render(request, "inicio.html", {'mensaje': f'Error al crear el usuario'})

    else:
            mi_formulario = UserCreationForm()           
            return render(request, "registro.html", {'pepe': mi_formulario})

# Perfil de usuario

def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':
        
        mi_formulario = UserRegisterForm(request.POST)
 
        if  mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"] 
            usuario.set_password(data["password1"])
            usuario.save()

            return render(request, "inicio.html", {'mensaje': f'Datos Actualizados'})

        return render(request, "editar_perfil.html", {'mensaje': f'Las Contraseñas no son iguales'})

    else:
            mi_formulario = UserRegisterForm(instance=request.user)           
    return render(request, "editar_perfil.html", {'pepe': mi_formulario})

# Clases

#Bebidas
class BebidaList(LoginRequiredMixin, ListView):
    model = Bebida
    template_name = 'bebidas_list.html'
    context_object_name = "bebidas"

class BebidaDetail(DetailView):
     model = Bebida
     template_name ='bebidas_detail.html'
     context_object_name = "bebida"

class BebidaCreate(CreateView):
     model = Bebida
     template_name = 'bebidas_create.html'
     fields = ["bebida", "precio"]
     success_url = '/bebidas_list'

class BebidaUpdate(UpdateView):
     model = Bebida
     template_name = 'bebidas_update.html'
     fields = ('__all__')
     success_url = '/bebidas_list'

class BebidaDelete(DeleteView):
     model = Bebida
     template_name = 'bebidas_delete.html'
     success_url = '/bebidas_list'


#Platos
class PlatoList(LoginRequiredMixin, ListView):
    model = Plato
    template_name = 'platos_list.html'
    context_object_name = "platos"

class PlatoDetail(DetailView):
     model = Plato
     template_name ='platos_detail.html'
     context_object_name = "platos"

class PlatoCreate(CreateView):
     model = Plato
     template_name = 'platos_create.html'
     fields = ["plato", "precio"]
     success_url = '/platos_list'

class PlatoUpdate(UpdateView):
     model = Plato
     template_name = 'platos_update.html'
     fields = ('__all__')
     success_url = '/platos_list'

class PlatoDelete(DeleteView):
     model = Plato
     template_name = 'platos_delete.html'
     success_url = '/platos_list'


#Postre

class PostreList(LoginRequiredMixin, ListView):
    model = Postre
    template_name = 'postres_list.html'
    context_object_name = "postres"

class PostreDetail(DetailView):
     model = Postre
     template_name ='postre_detail.html'
     context_object_name = "postre"

class PostreCreate(CreateView):
     model = Postre
     template_name = 'postre_create.html'
     fields = ["postre", "precio"]
     success_url = '/postres_list'

class PostreUpdate(UpdateView):
     model = Postre
     template_name = 'platos_update.html'
     fields = ('__all__')
     success_url = '/postres_list'

class PostreDelete(DeleteView):
     model = Postre
     template_name = 'postre_delete.html'
     success_url = '/postres_list'