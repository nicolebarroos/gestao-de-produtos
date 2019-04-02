from django.shortcuts import render, redirect
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
