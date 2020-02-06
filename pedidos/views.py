from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


def gestorLogin(request):
    return render(request, 'login.html')

def gestorLogout(request):
	logout(request)
	return redirect('/')

@csrf_protect
def gestor(request):
	username = request.POST.get('username')
	password = request.POST.get('password')

	user = authenticate(username=username, password=password)

	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect('/gestor/index')
	else:
		erro = "Usuário e/ou senha não cadastrados."
		context = {'erro': erro}
		return render(request, 'login.html', context)

	return redirect('/gestor')

@login_required(login_url='/')
def index(request):
	return render(request, 'gestor.html')

@login_required(login_url='/')
def gestorImportarPedido(request):
	request.FILES.get('file')
	return render(request, 'pedidos/import_order.html')

@login_required(login_url='/')
def gestorCadastrarCliente(request):
	return render(request, 'clientes/cadastro_clientes.html')

@login_required(login_url='/')
def gestorListarCliente(request):
	return render(request, 'clientes/listar_clientes.html')

@login_required(login_url='/')
def gestorCadastrarProdutos(request):
	return render(request, 'produtos/cadastro_produtos.html')

@login_required(login_url='/')
def gestorListarProdutos(request):
	return render(request, 'produtos/listar_produtos.html')

@login_required(login_url='/')
def gestorCadastrarFornecedores(request):
	return render(request, 'fornecedores/cadastro_fornecedores.html')

@login_required(login_url='/')
def gestorListarFornecedores(request):
	return render(request, 'fornecedores/listar_fornecedores.html')

@login_required(login_url='/')
def gestorCadastrarPedidos(request):
	return render(request, 'pedidos/cadastro_pedidos.html')

@login_required(login_url='/')
def gestorListarPedidos(request):
	return render(request, 'pedidos/listar_pedidos.html')