from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied

# Create your views here.

def index(request):
    template = loader.get_template('indexFeedback.html')
    return HttpResponse(template.render(RequestContext(request)))

def formularioFeedback(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            """send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )"""
            return redirect(reverse('index'))
    return render(request, 'contactUs.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })