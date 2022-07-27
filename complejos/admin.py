from django.contrib import admin
from complejos.models import Estadios, Parques
# Register your models here.

class EstadiosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'capacidad', 'num_camerinos', 'num_marcadores', 'num_cabinas_radio')
    
    search_fields = ('nombre','capacidad', 'capacidad', 'num_camerinos', 'num_marcadores', 'num_cabinas_radio')
    
admin.site.register(Estadios, EstadiosAdmin)


class ParquesAdmin(admin.ModelAdmin):
     list_display = ('nombre', 'direccion', 'tipo', 'num_monumentos')
     
     search_fields = ('nombre','direccion', 'tipo', 'num_monumentos')
      
admin.site.register(Parques, ParquesAdmin)
