from django.urls import path
from .views import listar_clientes, criar_clientes, update_clientes, delete_clientes

urlpatterns = [
    path('listar/', listar_clientes, name="listar_clientes"),
    path('criar/', criar_clientes, name="criar_clientes"),
    path('update/<int:id>/', update_clientes, name="update_clientes"),
    path('delete/<int:id>/', delete_clientes, name="delete_clientes"),

]