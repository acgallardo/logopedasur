from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from logopedasur.sesiones.forms import SesionesForm, nuevaSesionForm

# Create your views here.


def sesiones_list():
    pass


def sesiones_edit():
    pass

@login_required(login_url='/login/')
def sesiones_add(request):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
        initial = {}
        form = nuevaSesionForm(data=data, initial=initial)
        if form.is_valid():
            sesion= form.save(commit=False)
            sesion.paciente = request.paciente
            sesion.save()
            return HttpResponseRedirect(reverse(request.next))
#        return render_to_response("pacientes/tutor_add.html",{"form": form},context_instance=RequestContext(request))
