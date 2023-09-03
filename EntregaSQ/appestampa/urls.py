from django.urls import path
from EstampasVoodoo.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('clientes/', clientes, name="Clientes"),
    path('setCliente/', setCliente, name="setCliente"),
    path('getCliente/', getCliente, name="getCliente"),
    path('searchCliente/', searchCliente, name="searchCliente"),
    path('remeras/', remeras,name="Remeras"),
    path('setRemera/', setRemera, name="setRemera"),
    path('getRemera/', getRemera, name="getRemera"),
    path('searchRemera/', searchRemera, name="searchRemera"),
    path('tazas/', tazas, name="Tazas"),
    path('setTaza/', setTaza, name="setTaza"),
    path('getTaza/', getTaza, name="getTaza"),
    path('searchTaza/', searchTaza, name="searchTaza"),
]