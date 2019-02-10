from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto 
from .forms import ProdutoForm

def produtos_list(request):
    produtos = Produto.objects.all() #Seria como dar select*from no banco de dados
    return render(request, "produto.html", {'produtos' : produtos})

#Criando view para receber a criação dos novos produtos
def produtos_new(request):
    form = ProdutoForm(request.POST or None) #Receberá dos forms, onde vai fazer uma requisição post, caso não tenha: None,
    #onde vai criar um novo formulário:
    if form.is_valid():
        form.save()
        return redirect('produtos_list')
    return render(request, 'produtos_new.html', {'form': form})

def produtos_update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('produtos_list')
    return render(request, 'produtos_new.html', {'form': form})

def produtos_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('produtos_list')
    return render(request, 'produto_delete_confirm.html', {'produto': produto})

