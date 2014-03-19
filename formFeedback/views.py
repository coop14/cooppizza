from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied

from formFeedback.forms import FeedbackForm

# Create your views here.

def base(request):
    template = loader.get_template('formFeedback/base.html')
    return HttpResponse(template.render(RequestContext(request)))

def formularioFeedback(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'formFeedback/feedback.html', {
        'form': form,
    })

# OK ver como colocar campos com ingredientes disponiveis quando for adicionar ingrediente à pizza #
# colocar com tela bonitinha #
# OK definir tipos de pizza como doce, normal ou especial #
# verificar delete de bebida #
# OK ver coisa do unique (para nao poder cadastrar pizzas e ingredientes com mesmo nome) #
# NOT fazer pagina ilustrativa com listagem de pizzas e ingredientes #