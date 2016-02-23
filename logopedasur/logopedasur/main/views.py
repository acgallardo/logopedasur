from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
def index(request):
    return render_to_response("main/index.html",
            {"nombre": "trukise"},
            context_instance=RequestContext(request))
