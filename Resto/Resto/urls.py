"""Resto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from AppResto.views import *  


#from AppResto.views import inicio, curso, bebida, postre, plato, lista_curso, lista_bebida, lista_postre, lista_plato,bebidas, platos, postres, bebidaFormulario, busqueda_bebida,buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name="Inicio"),

    #Secciones
    path('bebidas/', bebidas, name="Bebidas"),
    path('platos/', platos, name="Platos"),
    path('postres/', postres, name="Postres"),
    
    #Altas    
    path('agrega-curso/<nombre>/<camada>', curso),
    path('agrega-bebida/<bebida>/<precio>', bebida),
    path('agrega-postre/<postre>/<precio>', postre),
    path('agrega-plato/<plato>/<guarnicion>/<precio>', plato),

    #Listados
    path('lista-curso/', lista_curso),
    path('lista-bebida/', lista_bebida),
    path('lista-postre/', lista_postre),
    path('lista-plato/', lista_plato),

    path('leerBebidas/', leerBebidas, name="LeerBebidas"),

    #Formularios
    path('bebidaFormulario/', bebidaFormulario, name='bebidaFormulario'),

    #Busquedas
    path('busqueda_bebida/', busqueda_bebida, name='busqueda_bebida'),
    path('buscar_bebida/', buscar_bebida, name='buscar_bebida'),
    path('busqueda_camada/', busqueda_camada, name='busqueda_camada'),
    path('buscar/', buscar, name='buscar'),

    #CREATE
    path('crea_bebida/', crea_bebida, name='Crea_bebida'),

    #DELETE
    path('elimina_bebida/<int:id>', eliminar_bebida, name='Elimina_bebida'),

    #UPDATE
    path('editar_bebida/<int:id>', editar_bebida, name='Editar_bebida'),

    #CLASS
    path('bebidas_list', BebidaList.as_view(), name='Bebidas_list'),
    path('detalleBebida/<pk>', BebidaDetail.as_view(), name='DetalleBebida'),
    path('creaBebida/', BebidaCreate.as_view(), name='CreaBebida'),
    path('actualizarBebida/<pk>', BebidaUpdate.as_view(), name='ActualizaBebida'),
    path('eliminarBebida/<pk>', BebidaDelete.as_view(), name='EliminaBebida'),
    
    #LOGIN/LOGOUT
    path('login/', loginView, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='Logout'),


    #Perfil de Usuario
    path('  /', editar_perfil, name='Editar Perfil'),   
]