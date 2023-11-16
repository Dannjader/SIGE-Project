from django.urls import path
from dispositivos.views import inicio, dispositivos_list, servicios_list

urlpatterns = [
    path('', inicio, name='inicio'),
    path('dispositivos/', dispositivos_list, name='dispositivos'),
    path('servicios/', servicios_list, name='servicios'),
]
