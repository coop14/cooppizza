from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext, loader
from django.http.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied

from pedidos.models import Produto, Pedido, Pizza, Ingrediente, Bebida, PizzaIngrediente, Pagamento, PromocoesDaPizzaria

def pagar(request, pedido_id):
    p = get_object_or_404(Pagamento, pk=pagamento_id)
    try:
        selected_pagamento = p.pagamento_set.get(pk=request.POST['pagamento'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'pedidos/tempale_forma_pagamento/formulario.html', {
            'pagamento': p,
            'error_message': "Não selecionaste o pagamento.",
        })
    else:
        selected_pagamento.pagamento += 1
        selected_pagamento.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pagamento:pa', args=(p.id,)))
