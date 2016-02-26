from datetime import datetime

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext


from logopedasur.terapeutas.models import Terapeuta
from logopedasur.terapeutas.models import Especialidad
from logopedasur.terapeutas.forms import TerapeutasForm, EspecialidadesForm

# Create your views here.


def terapeutas_list(request):
    terapeutas = Terapeuta.objects.filter().order_by('apellidos')
    return render_to_response("terapeutas/terapeutas_list.html",
                              {"terapeutas": terapeutas},
                              context_instance=RequestContext(request))


@login_required(login_url='/login/')
def terapeutas_add(request):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
    initial = {}
    form = TerapeutasForm(data=data, initial=initial)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('terapeutas_list'))
    return render_to_response("terapeutas/terapeutas_add.html",
                                                            {"nombre": "trukise", "form": form},
                                                            context_instance = RequestContext(request))

@login_required(login_url='/login/')
def especialidad_add(request):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
    initial = {}
    form = EspecialidadesForm(data=data, initial=initial)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('especialidad_list'))
    return render_to_response("terapeutas/especialidad_add.html",
                                                            {"nombre": "trukise", "form": form},
                                                            context_instance= RequestContext(request))


@login_required(login_url='/login/')
def especialidad_list(request):
    especialidades = Especialidad.objects.filter().order_by('nombre')
    return render_to_response("terapeutas/especialidad_list.html",
                                                            {"especialidades": especialidades},
                                                            context_instance= RequestContext(request))


def terapeutas_details(request, terapeutasitem_pk):
    pass


@login_required(login_url='/admin/')
def terapeutas_edit(request, terapeutasitem_pk):
    pass
