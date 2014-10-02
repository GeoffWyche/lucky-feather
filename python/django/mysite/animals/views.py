from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from animals.models import TreeNode
from animals.dumbDOM import gDOM, gHead, gBody, gText, gBodyText, gButton

# Note: yes, you really do have to supply the entire HTML document.
# Get to work! (use django's templates)
# see file:///C:/Users/Geoff/python/django-example/ref/template-response.html
# www.w3schools.com

head = gHead("Animals Game")

#def index(request):
#    t = TreeNode.objects.get(id='1')
#    dom = gDOM(head,
#               body=gBody([gBodyText(t.node_text),
#                           gButton(label='Yes',nodeid=t.yes_link.id.__str__()),
#                           gButton(label='No',nodeid=t.no_link.id.__str__())]
#                          ))
#    return HttpResponse(dom.render())

def guess(request,currnode='1'):
    cn = TreeNode.objects.get(id=currnode)

    if cn.is_animal:
        q = "Is the animal you're thinking of "
        q += cn.article()
        q += " " + cn.node_text + "?"
        dom = gDOM(head,
                   body=gBody([gBodyText(q),
                               gBodyText("<p>"),
                               gButton(label='Yes',nodeid='0'),
                               gBodyText("<p>"),
                               gButton(label='No',nodeid='0')]
                          ))
    else:
        dom = gDOM(head,
                   body=gBody([gBodyText(cn.node_text),
                               gBodyText("<p>"),
                               gButton(label='Yes',nodeid=cn.yes_link.id.__str__()),
                               gBodyText("<p>"),
                               gButton(label='No',nodeid=cn.no_link.id.__str__())]
                          ))
    return HttpResponse(dom.render())
