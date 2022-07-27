from django import forms
from complejos.models import Parques, Estadios

class ParquesForm(forms.ModelForm):
    class Meta:
        model = Parques
        fields = ['nombre', 'direccion', 'tipo', 'num_monumentos',]
        
   
        
        
        
class EstadiosForm(forms.ModelForm):
    class Meta:
        model = Estadios
        fields = ['nombre', 'capacidad', 'num_camerinos', 'num_marcadores', 'num_cabinas_radio', 'direccion',]
        
    