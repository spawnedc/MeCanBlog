from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    """ basic homepage view """
    template_vars = {}
    template_vars['test'] = 'test'
    return render_to_response("home.html", template_vars, RequestContext(request))