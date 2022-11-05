from django.contrib import admin
from django.urls import path
from .views import platoPpal, bebida, postre,inicio, bebidaFormulario,postreFormulario,platoPpalFormulario,busqueda_bebida,buscar_bebida, busqueda_postre, buscar_postre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('bebidas/', bebida, name='bebidas'),
    path('postres/', postre, name='postre'),
    path('platoPpal/', platoPpal, name='platoPpal'),
    path('lista_bebidas/', bebida, name='bebidas'),
    path('bebidaFormulario/', bebidaFormulario, name='bebidaFormulario'),
    path('postreFormulario/', postreFormulario, name='postreFormulario'),
    path('platoPpalFormulario/', platoPpalFormulario, name='platoPpalFormulario'),

    path('busqueda_bebida/', busqueda_bebida, name='busqueda_bebida'),
    path('buscar_bebida/', buscar_bebida, name='buscar_bebida'),
    
    path('busqueda_postre/', busqueda_postre, name='busqueda_postre'),
    path('buscar_postre/', buscar_postre, name='buscar_postre'),
]