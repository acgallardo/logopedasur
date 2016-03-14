from django.conf.urls import patterns, url


urlpatterns = patterns(
    'logopedasur.pacientes.views',
    # url (<patron>, funcion, url)
    url(r'^pacientes/add/$', 'pacientes_add', name='pacientes_add'),
    url(r'^pacientes/edit/(?P<pacientesitem_pk>\d+)/$', 'pacientes_edit', name='pacientes_edit'),
    url(r'^pacientes/details/(?P<pacientesitem_pk>\d+)/$', 'pacientes_details', name='pacientes_details'),
    url(r'^pacientes/details/(?P<pacientesitem_pk>\d+)/sesion/add/$', 'pacientes_sesion_add', name='pacientes_sesion__add'),
    url(r'^pacientes/details/(?P<pacientesitem_pk>\d+)/informe/add/$', 'pacientes_informe_add', name='pacientes_informe_add'),
    url(r'^pacientes/$', 'pacientes_list', name='pacientes_list'),
    url(r'^pacientes/tutor/add/$', 'tutor_add', name='tutor_add'),
    url(r'^pacientes/tutores/$', 'tutores_list', name='tutores_list'),
    url(r'^pacientes/tutores/details/(?P<tutoresitem_pk>\d+)/$', 'tutores_details', name='tutores_details'),

)
