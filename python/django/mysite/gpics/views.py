from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    answer = 42
    template = loader.get_template('gpics/index.html')
    context = RequestContext(request, {
        'g1': answer,
    })
    return HttpResponse(template.render(context))
