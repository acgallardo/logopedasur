from datetime import datetime

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from logopedasur.pacientes.models import Paciente, Tutor
from logopedasur.sesiones.models import Sesion
from logopedasur.pacientes.forms import PacientesForm, TutoresForm


@login_required(login_url="/login/")
def tutores_list(request):
    tutores = Tutor.objects.filter().order_by('apellidos')
    return render_to_response("pacientes/tutores_list.html",
                              {'tutores': tutores},
                              context_instance=RequestContext(request))


@login_required(login_url="/login/")
def tutor_add(request):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
    initial = {}
    form = TutoresForm(data=data, initial=initial)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('pacientes_list'))
    return render_to_response("pacientes/tutor_add.html",{"form": form},context_instance=RequestContext(request))


def pacientes_details(request, pacientesitem_pk):
    paciente = Paciente.objects.get(pk=pacientesitem_pk)
    sesiones_paciente = Sesion.objects.filter(paciente__pk=pacientesitem_pk)
    return render_to_response("pacientes/pacientes_details.html",
                              {'paciente': paciente,
                               'sesiones_paciente': sesiones_paciente},
                              context_instance=RequestContext(request))


def pacientes_list(request):
    pacientes = Paciente.objects.filter().order_by('apellidos')
    return render_to_response("pacientes/pacientes_list.html",
                              {'nombre': 'trukise', 'pacientes': pacientes},
                              context_instance=RequestContext(request))


@login_required(login_url='/login/')
def pacientes_add(request):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
    initial = {}
    form = PacientesForm(data=data, initial=initial)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('pacientes_list'))
    return render_to_response("pacientes/pacientes_add.html",{"nombre": "trukise", "form": form},context_instance=RequestContext(request))


@login_required(login_url='/admin/')
def pacientes_edit(request, pacientesitem_pk):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
    pacientes_item = Paciente.objects.get(pk=pacientesitem_pk)
    form = PacientesForm(data=data, instance=pacientes_item)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('pacientes_list'))
    return render_to_response("pacientes/pacientes_add.html",{'form': form},context_instance=RequestContext(request))

# Create your views here.
