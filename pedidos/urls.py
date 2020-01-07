from django.urls import path
from .views import gestorLogin,gestorLogout,gestor,index,gestorImportarPedido,gestorCadastrarCliente,gestorListarCliente,gestorCadastrarProdutos,gestorCadastrarFornecedores,gestorListarProdutos,gestorListarFornecedores,gestorCadastrarPedidos,gestorListarPedidos

app_name = 'pedidos'

urlpatterns =[
    path('', gestorLogin, name='gestorLogin'),
    path('logout', gestorLogout, name='gestorlogout'),

    path('gestor', gestor, name='gestor'),
    path('gestor/pedidos/importar', gestorImportarPedido, name='importarpedido'),
    path('gestor/pedidos/cadastrar', gestorCadastrarPedidos, name='cadastropedido'),
    path('gestor/pedidos/listar', gestorListarPedidos, name='listarpedido'),

    path('gestor/clientes/cadastrar', gestorCadastrarCliente, name='cadastrocliente'),
    path('gestor/clientes/listar', gestorListarCliente, name='listarcliente'),

    path('gestor/produtos/cadastrar', gestorCadastrarProdutos, name='cadastroproduto'),
    path('gestor/produtos/listar', gestorListarProdutos, name='listarproduto'),

    path('gestor/fornecedores/cadastrar', gestorCadastrarFornecedores, name='cadastrofornecedor'),
    path('gestor/fornecedores/listar', gestorListarFornecedores, name='listarfornecedor'),

    path('gestor/index', index, name='index'),
]