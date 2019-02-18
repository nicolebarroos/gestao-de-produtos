from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto 
from .forms import ProdutoForm

@login_required
def produtos_list(request):
    termo_busca = request.GET.get('pesquisa', None)#requeste get para buscar dado 
    #'pesquisa' é referenciado no meu template como id do campo de busca

    if termo_busca:
        produtos = Produto.objects.all() #Seria como dar select*from no banco de dados
        produtos = produtos.filter(nome__icontains=termo_busca)
    else:
        produtos = Produto.objects.all()
    return render(request, "produto.html", {'produtos' : produtos})

@login_required
#Criando view para receber a criação dos novos produtos
def produtos_new(request):
    form = ProdutoForm(request.POST or None) #Receberá dos forms, onde vai fazer uma requisição post, caso não tenha: None,
    #onde vai criar um novo formulário:
    if form.is_valid():
        form.save()
        return redirect('produtos_list')
    return render(request, 'produtos_new.html', {'form': form})

@login_required
def produtos_update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('produtos_list')
    return render(request, 'produtos_new.html', {'form': form})

@login_required
def produtos_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('produtos_list')
    return render(request, 'produto_delete_confirm.html', {'produto': produto})

