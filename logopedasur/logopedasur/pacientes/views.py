from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from logopedasur.pacientes.models import Paciente
from logopedasur.pacientes.forms import PacientesForm

# Create your views here.
def pacientes_list(request):
    pacientes = Paciente.objects.filter(publish_date__lte=datetime.now()).order_by('-publish_date')
    return render_to_response("pacientes/pacientes_list.html",
    {'pacientes': pacientes},
    context_instance=RequestContext(request))

def pacientes_add(request):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
    initial = {}
    form = PacientesForm(data=data, initial=initial)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('pacientes_list'))
    return render_to_response("pacientes/pacientes_add.html",{'form': form},context_instance=RequestContext(request))


def pacientes_edit(request, newsitem_pk):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
    news_item = News.objects.get(pk=newsitem_pk)
    form = NewsForm(data=data, instance=news_item)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('news_list'))
    return render_to_response("news/news_add.html",{'form': form},context_instance=RequestContext(request))

# Create your views here.
