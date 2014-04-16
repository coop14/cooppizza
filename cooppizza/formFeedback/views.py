from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from forms import FeedbackForm

# Create your views here.

def indexFeedback(request):
    template = loader.get_template('indexFeedback.html')
    return HttpResponse(template.render(RequestContext(request)))

def formularioFeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            assunto = forms.cleaned_data['assunto']
            message = form.cleaned_data['message']
            dataDoFeedback =  forms.cleaned_data['dataDoFeedback']
            tipoDePedido = forms.cleaned_data['tipoDePedido']
            formaDePedido = forms.cleaned_data['formaDePedido']
            precoPedido = forms.cleaned_data['precoPedido']
            observacoes = forms.cleaned_data['observacoes']
            nota = forms.cleaned_data['nota']
            email = form.cleaned_data['email']
            """if cc_myself:
            recipients.append(sender)
            send_mail(subject, message, sender, recipients)"""
            return HttpResponseRedirect('obrigado.html')
    else:
        form = FeedbackForm() 

    return render(request, 'contactUs.html', {
        'form': form,
    })

def obrigado(request):
    template = loader.get_template('obrigado.html')
    return HttpResponse(template.render(RequestContext(request)))

