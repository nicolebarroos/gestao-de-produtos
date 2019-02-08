from django.urls import path
from .views import produtos_list
from .views import produtos_new
from .views import produtos_update
from .views import produtos_delete

urlpatterns = [
    path('list/', produtos_list, name="produtos_list"),
    path('new/', produtos_new, name="produtos_new"), #Criando uma url para criação dos produtos
    path('update/<int:id>/', produtos_update, name="produtos_update"),
    path('delete/<int:id>/', produtos_delete, name="produtos_delete")

]
