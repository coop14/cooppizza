from django.conf.urls import patterns, include, url
from cardapio import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^base$', views.base, name='base'),
	url(r'^pizza$', views.pizza, name='pizza'),
	url(r'^bebida$', views.bebida, name='bebida'),
	url(r'^ingrediente$', views.ingrediente, name='ingrediente'),
	url(r'^ingrediente/novo$', views.ingredienteNovo, name='ingredienteNovo'),
	url(r'^ingrediente/consulta$', views.ingredienteConsulta, name='ingredienteConsulta'),
	url(r'^ingrediente/cadastrar$', views.ingredienteCadastrar, name='ingredienteCadastrar'),
	url(r'^ingrediente/(?P<ingrediente_id>\d+)/editar$', views.ingredienteEdita, name='ingredienteEdita'),
	url(r'^ingrediente/(?P<ingrediente_id>\d+)/alterar$', views.ingredienteAltera, name='ingredienteAltera'),
	url(r'^ingrediente/(?P<ingrediente_id>\d+)$', views.ingredienteDados, name='ingredienteDados'),
	url(r'^ingrediente/(?P<ingrediente_id>\d+)/deletar$', views.ingredienteDeletar, name='ingredienteDeletar'),
	url(r'^pizza/nova$', views.pizzaNova, name='pizzaNova'),
	url(r'^pizza/consulta$', views.pizzaConsulta, name='pizzaConsulta'),
	url(r'^pizza/cadastrar$', views.pizzaCadastrar, name='pizzaCadastrar'),
	url(r'^pizza/(?P<pizza_id>\d+)$', views.pizzaDados, name='pizzaDados'),
	url(r'^pizza/(?P<pizza_id>\d+)/editar$', views.pizzaEdita, name='pizzaEdita'),
	url(r'^pizza/(?P<pizza_id>\d+)/alterar$', views.pizzaAltera, name='pizzaAltera'),
	url(r'^pizza/(?P<pizza_id>\d+)/ingredienteDaPizza$', views.pizzaIngrediente, name='pizzaIngrediente'),
	url(r'^pizza/(?P<pizza_id>\d+)/adicionar$', views.pizzaIngredienteAdiciona, name='pizzaIngredienteAdiciona'),
	url(r'^pizza/(?P<pizza_id>\d+)/deletar$', views.pizzaDeletar, name='pizzaDeletar'),
	url(r'^pizza/(?P<pizza_id>\d+)/(?P<pizzaingrediente_id>\d+)/deletarIngrediente$', views.pizzaDeletarIngrediente, name='pizzaDeletarIngrediente'),
	url(r'^bebida/nova$', views.bebidaNova, name='bebidaNova'),
	url(r'^bebida/consulta$', views.bebidaConsulta, name='bebidaConsulta'),
	url(r'^bebida/cadastrar$', views.bebidaCadastrar, name='bebidaCadastrar'),
	url(r'^bebida/(?P<bebida_id>\d+)$', views.bebidaDados, name='bebidaDados'),
	url(r'^bebida/(?P<bebida_id>\d+)/editar$', views.bebidaEdita, name='bebidaEdita'),
	url(r'^bebida/(?P<bebida_id>\d+)/alterar$', views.bebidaAltera, name='bebidaAltera'),
	url(r'^bebida/(?P<bebida_id>\d+)/deletar$', views.bebidaDeletar, name='bebidaDeletar'),
	url(r'^lista$', views.listaProduto, name='lista'),
)
