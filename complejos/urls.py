from django.urls import path
from complejos.views import eliminarEstadios, eliminarParques, index, crearParque, listarParque, crearEstadios, listarEstadios, \
editarParque, editarEstadios

app_name = 'complejos'
 
urlpatterns = [
   
    path('', index, name='index'),
    
    # Parques
    path('crear-parque', crearParque, name='crear-parque'),
    path('listar-parque', listarParque, name='listar-parque'),
    path('editar-parque/<id_parque>', editarParque, name='editar-parque/<id_parque>'),
    path('eliminar-parque/<id_parque>', eliminarParques, name='eliminar-parque/<id_parque>'),
    
    #Estadios
    path('crear-estadios', crearEstadios, name='crear-estadios'),
    path('listar-estadios', listarEstadios, name='listar-estadios'),
    path('editar-estadios/<id_estadios>', editarEstadios, name='editar-estadios/<id_estadios>'),
    path('eliminar-estadios/<id_estadios>', eliminarEstadios, name='eliminar-estadios/<id_estadios>')
    
]
