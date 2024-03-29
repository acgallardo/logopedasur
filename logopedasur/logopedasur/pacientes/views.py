from datetime import datetime

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext


from logopedasur.pacientes.models import Paciente, Tutor, Informe
from logopedasur.sesiones.models import Sesion
from logopedasur.facturacion.models import Factura, FacturaDetalle
from logopedasur.pacientes.forms import PacientesForm, TutoresForm, NuevoInformeForm
from logopedasur.sesiones.forms import SesionesForm, nuevaSesionForm

@login_required(login_url="/login/")
def tutores_list(request):
    letras = map(chr, range(65, 91))
    encontradas = []

    for l in letras:
        tutores = Tutor.objects.filter(nombre__startswith=l)
        if tutores:
            encontradas.append(l)
    if request.GET.get('initial'):
        tutores = Tutor.objects.filter(nombre__startswith=request.GET.get('initial'))
    else:
        tutores = Tutor.objects.filter().order_by('apellidos')

    paginator = Paginator(tutores, settings.TUTORES_PAGINATION_PAGES)
    page = request.GET.get('page')
    try:
        tutores = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        tutores = paginator.page(1)
    except EmptyPage:
        #if page is out of range , deliver last page of results
        tutores = paginator.page(paginator.num_pages)
    return render_to_response("pacientes/tutores_list.html",
                              {"username": request.user, 'tutores': tutores,
                               "encontradas": encontradas},
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
    return render_to_response("pacientes/tutor_add.html",{"username": request.user, "form": form},context_instance=RequestContext(request))

@login_required(login_url="/login/")
def tutores_details(request, tutoresitem_pk):
    tutor = Tutor.objects.get(pk=tutoresitem_pk)
    pacientes = Paciente.objects.filter(tutor__pk=tutoresitem_pk)
    return render_to_response("pacientes/tutores_details.html",
                               {"username": request.user,
                                'tutor': tutor,
                                'pacientes': pacientes},
                               context_instance=RequestContext(request))


@login_required(login_url="/login/")
def pacientes_details(request, pacientesitem_pk):
    paciente = Paciente.objects.get(pk=pacientesitem_pk)

    sesiones_paciente = Sesion.objects.filter(paciente__pk=pacientesitem_pk)
    paginator_sesiones = Paginator(sesiones_paciente, settings.SESIONES_PAGINATION_PAGES)
    page = request.GET.get('page')
    try:
        sesiones_paciente = paginator_sesiones.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        sesiones_paciente = paginator_sesiones.page(1)
    except EmptyPage:
        #if page is out of range , deliver last page of results
        sesiones_paciente = paginator_sesiones.page(paginator_sesiones.num_pages)

    informes_paciente = Informe.objects.filter(paciente__pk=pacientesitem_pk)
    paginator_informes = Paginator(informes_paciente, settings.INFORMES_PAGINATION_PAGES)
    page = request.GET.get('page')
    try:
        informes_paciente = paginator_informes.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        informes_paciente = paginator_informes.page(1)
    except EmptyPage:
        #if page is out of range , deliver last page of results
        informes_paciente = paginator_informes.page(paginator_informes.num_pages)

    facturas_paciente = Factura.objects.filter(paciente__pk=pacientesitem_pk)
    paginator_facturas = Paginator(facturas_paciente, settings.FACTURAS_PAGINATION_PAGES)
    page = request.GET.get('page')
    try:
        facturas_paciente = paginator_facturas.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        facturas_paciente = paginator_facturas.page(1)
    except EmptyPage:
        #if page is out of range , deliver last page of results
        facturas_paciente = paginator_facturas.page(paginator_facturas.num_pages)

    # Create nnuevaSesionForm and only show the patient relationed
    # on manytomany form field, using initial values, a populate "paciente"
    # fields with specified values with a queryset
    data_sesion = None
    initial_sesion = {'paciente': Paciente.objects.get(pk=pacientesitem_pk)}
    formNuevaSesion = nuevaSesionForm(data=data_sesion, initial=initial_sesion)
    formNuevaSesion.fields['paciente'].queryset = Paciente.objects.filter(pk=pacientesitem_pk)

    # Create NuevoInformeForm and only show the patient relationed
    # using initial values, and populate "paciente"
    # fields with specified values with a queryset
    data_informe = None
    initial_informe = {'paciente': Paciente.objects.get(pk=pacientesitem_pk)}
    formNuevoInforme = NuevoInformeForm(data=data_informe, initial=initial_informe)
    formNuevoInforme.fields['paciente'].queryset = Paciente.objects.filter(pk=pacientesitem_pk)

    if request.GET.get('tab') == 'sesiones':
        tab_active = "sesiones"
    elif request.GET.get('tab') == 'facturas':
        tab_active = "facturas"
    elif request.GET.get('tab') == 'informes':
        tab_active = "informes"
    else:
        tab_active = "observaciones"

    return render_to_response("pacientes/pacientes_details.html",
                              {"username": request.user,
                               'paciente': paciente,
                               'sesiones_paciente': sesiones_paciente,
                               'informes_paciente': informes_paciente,
                               'facturas_paciente': facturas_paciente,
                               'formNuevaSesion': formNuevaSesion,
                               'formNuevoInforme': formNuevoInforme,
                               'tab_active': tab_active},
                               context_instance=RequestContext(request))

@login_required(login_url="/login")
def pacientes_list(request):

    letras = map(chr, range(65, 91))
    encontradas = []

    for l in letras:
        pacientes = Paciente.objects.filter(nombre__startswith=l)
        if pacientes:
            encontradas.append(l)

    if request.GET.get('initial'):
        pacientes = Paciente.objects.filter(nombre__startswith=request.GET.get('initial'))
    else:
        pacientes = Paciente.objects.filter().order_by('apellidos')
    paginator = Paginator(pacientes, settings.PACIENTES_PAGINATION_PAGES)
    page = request.GET.get('page')
    try:
        pacientes = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        pacientes = paginator.page(1)
    except EmptyPage:
        #if page is out of range , deliver last page of results
        pacientes = paginator.page(paginator.num_pages)

    return render_to_response("pacientes/pacientes_list.html",
                              {"username": request.user,
                               'pacientes': pacientes,
                               'encontradas': encontradas},
                              context_instance=RequestContext(request))


@login_required(login_url='/login/')
def pacientes_add(request):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
    initial = {}
    form = PacientesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('pacientes_list'))
    return render_to_response("pacientes/pacientes_add.html",{"username": request.user, "form": form, "action":"insertar"},context_instance=RequestContext(request))


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
    return render_to_response("pacientes/pacientes_add.html",{"username": request.user,'form': form, "action":"editar"},context_instance=RequestContext(request))

@login_required(login_url="/admin/")
def pacientes_sesion_add(request, pacientesitem_pk):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
        initial = {}
        form = nuevaSesionForm(data=data, initial=initial)
        if form.is_valid():
            form.save()
        paciente = Paciente.objects.get(pk=pacientesitem_pk)
        sesiones_paciente = Sesion.objects.filter(paciente__pk=pacientesitem_pk)
        data = None
        initial = {'paciente': Paciente.objects.get(pk=pacientesitem_pk)}
        formNuevoInforme = NuevoInformeForm(data=data, initial=initial)
        formNuevoInforme.fields['paciente'].queryset = Paciente.objects.filter(pk=pacientesitem_pk)
        formNuevaSesion = nuevaSesionForm(data=data, initial=initial)
        formNuevaSesion.fields['paciente'].queryset = Paciente.objects.filter(pk=pacientesitem_pk)
        return render_to_response("pacientes/pacientes_details.html",
                                  {"username": request.user,
                                   'paciente': paciente,
                                   'sesiones_paciente': sesiones_paciente,
                                   'formNuevaSesion': formNuevaSesion,
                                   'formNuevoInforme': formNuevoInforme,
                                   'tab_active': "sesiones"},
                                   context_instance=RequestContext(request))


@login_required(login_url="/admin/")
def pacientes_informe_add(request, pacientesitem_pk):
    data = None #por si no hubiera un POST
    if request.method == 'POST':
        data = request.POST
        initial = {}
        formNuevoInforme = NuevoInformeForm(request.POST, request.FILES)
        if formNuevoInforme.is_valid():
            formNuevoInforme.save()


        paciente = Paciente.objects.get(pk=pacientesitem_pk)

        sesiones_paciente = Sesion.objects.filter(paciente__pk=pacientesitem_pk)
        paginator_sesiones = Paginator(sesiones_paciente, settings.SESIONES_PAGINATION_PAGES)
        page = request.GET.get('page')
        try:
            sesiones_paciente = paginator_sesiones.page(page)
        except PageNotAnInteger:
            # if page is not an integer, deliver first page
            sesiones_paciente = paginator_sesiones.page(1)
        except EmptyPage:
            #if page is out of range , deliver last page of results
            sesiones_paciente = paginator_sesiones.page(paginator_sesiones.num_pages)

        informes_paciente = Informe.objects.filter(paciente__pk=pacientesitem_pk)
        paginator_informes = Paginator(informes_paciente, settings.INFORMES_PAGINATION_PAGES)
        page = request.GET.get('page')
        try:
            informes_paciente = paginator_informes.page(page)
        except PageNotAnInteger:
            # if page is not an integer, deliver first page
            informes_paciente = paginator_informes.page(1)
        except EmptyPage:
            #if page is out of range , deliver last page of results
            informes_paciente = paginator_informes.page(paginator_informes.num_pages)

        facturas_paciente = Factura.objects.filter(paciente__pk=pacientesitem_pk)
        paginator_facturas = Paginator(facturas_paciente, settings.FACTURAS_PAGINATION_PAGES)
        page = request.GET.get('page')
        try:
            facturas_paciente = paginator_facturas.page(page)
        except PageNotAnInteger:
            # if page is not an integer, deliver first page
            facturas_paciente = paginator_facturas.page(1)
        except EmptyPage:
            #if page is out of range , deliver last page of results
            facturas_paciente = paginator_facturas.page(paginator_facturas.num_pages)

        data = None
        initial = {'paciente': Paciente.objects.get(pk=pacientesitem_pk)}
        formNuevaSesion = nuevaSesionForm(data=data, initial=initial)
        formNuevaSesion.fields['paciente'].queryset = Paciente.objects.filter(pk=pacientesitem_pk)
        formNuevoInforme.fields['paciente'].queryset = Paciente.objects.filter(pk=pacientesitem_pk)
        return render_to_response("pacientes/pacientes_details.html",
                                  {"username": request.user,
                                   'paciente': paciente,
                                   'sesiones_paciente': sesiones_paciente,
                                   'informes_paciente': informes_paciente,
                                   'facturas_paciente': facturas_paciente,
                                   'formNuevaSesion': formNuevaSesion,
                                   'formNuevoInforme': formNuevoInforme,
                                   'tab_active': "informes"},
                                   context_instance=RequestContext(request))
