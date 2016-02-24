from django.conf.urls import patterns, url

urlpatterns = patterns(
    'logopedasur.terapeutas.views',
    # url (<patron>, funcion, url)
    url(r'^terapeutas/add/$', 'terapeutas_add', name='terapeutas_add'),
    url(r'^terapeutas/edit/(?P<terapeutasitem_pk>\d+)/$', 'terapeutas_edit', name='terapeutas_edit'),
    url(r'^terapeutas/details/(?P<terapeutasitem_pk>\d+)/$', 'terapeutas_details', name='terapeutas_details'),
    url(r'^terapeutas/$', 'terapeutas_list', name='terapeutas_list'),

)
