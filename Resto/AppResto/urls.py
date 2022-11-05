from django.contrib import admin
from django.urls import path
from .views import platoPpal, bebida, postre,inicio, bebidaFormulario,postreFormulario,platoPpalFormulario,busquedaBebida,buscarBebidas

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
    path('busquedaBebida/', busquedaBebida, name='busquedaBebida'),
    path('buscarbebida/', buscarBebidas, name='buscarbebida'),
]