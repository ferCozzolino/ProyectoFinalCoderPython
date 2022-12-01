from django.contrib import admin
from .models import Plato, Bebida, Postre, Avatar

# Register your models here.
admin.site.register(Plato)
admin.site.register(Bebida)
admin.site.register(Postre)
admin.site.register(Avatar)