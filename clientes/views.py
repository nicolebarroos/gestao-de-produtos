from django.shortcuts import render, redirect, get_object_or_404
from .models import Cadastro
from .forms import CadastroForm

def listar_clientes(request):
    cadastro = Cadastro.objects.all()
    footer_mensage = "Desenvolvimento django 2.1"
    return render(request, 'cliente.html', {'cadastro': cadastro, 'footer_mensage':footer_mensage})

def criar_clientes(request):
    #checar permissão dentro de usuário
    #if not request.user.has_perm('clientes.add_person'):
    #    return HttpResponse('Não autorizado')

    form = CadastroForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'cliente_form.html', {'form': form})

def update_clientes(request, id):
    cadastro = get_object_or_404(Cadastro, pk=id)
    form = CadastroForm(request.POST or None, request.FILES or None, instance=cadastro)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'cliente_form.html', {'form': form})

def delete_clientes(request, id):
    cadastro = get_object_or_404(Cadastro, pk=id)

    if request.method == 'POST':
        cadastro.delete()
        return redirect('listar_clientes')

    return render(request, 'confirmar_deleção.html', {'cadastro': cadastro})



