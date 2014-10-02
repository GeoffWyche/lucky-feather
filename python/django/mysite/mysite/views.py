from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.staticfiles import finders

def home(request):
    template = loader.get_template('mysite/index.html')
    context = RequestContext(request, {
    })
    rval = template.render(context)
#    result = finders.find('mysite/style.css')
#    for r in result.searched_locations:
#        print(r)
    return HttpResponse(rval)
