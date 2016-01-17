from django.conf.urls import patterns, url


urlpatterns = patterns(
    'logopedasur.pacientes.views',
    # url (<patron>, funcion, url)
    url(r'^pacientes/add/$', 'pacientes_add', name='pacientes_add'),
    url(r'^pacientes/edit/(?P<pacientesitem_pk>\d+)/$', 'pacientes_edit', name='pacientes_edit'),
    url(r'^pacientes/$', 'pacientes_list', name='pacientes_list'),
)
