from django.contrib import admin
from django.urls import path
from .views import platoPpal, bebida, postre,inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('agrega-combo/<combo>/<plato>/<guarnicion>/<precio>', platoPpal, name='platoppal'),
    path('bebidas/', bebida, name='bebidas'),
    path('postres/', postre, name='postre'),
   #path('platos/', platos, name='platos'),
]