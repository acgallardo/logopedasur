from datetime import datetime

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext


from logopedasur.terapeutas.models import Terapeuta
from logopedasur.terapeutas.models import Especialidad

# Create your views here.


def terapeutas_list(request):
    terapeutas = Terapeuta.objects.filter().order_by('apellidos')
    return render_to_response("terapeutas/terapeutas_list.html",
                              {"terapeutas": terapeutas},
                              context_instance=RequestContext(request))
@login_required(login_url='/login/')
def terapeutas_add(request, terapeutasitem_pk):
    pass


def terapeutas_details(request, terapeutasitem_pk):
    pass

@login_required(login_url='/admin/')
def terapeutas_edit(request, terapeutasitem_pk):
    pass
