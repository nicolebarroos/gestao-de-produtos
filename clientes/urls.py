from django.urls import path
from .views import listar_clientes, criar_clientes

urlpatterns = [
    path('listar/', listar_clientes, name="listar_clientes"),
    path('criar/', criar_clientes, name="criar_clientes"),

]