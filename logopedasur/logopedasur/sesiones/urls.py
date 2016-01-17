from django.conf.urls import patterns, url


urlpatterns = patterns(
    'logopedasur.sesiones.views',
    # url (<patron>, funcion, url)
    url(r'^sesiones/add/$', 'sesiones_add', name='sesiones_add'),
    url(r'^sesiones/edit/(?P<sesionesitem_pk>\d+)/$', 'sesiones_edit', name='sesiones_edit'),
    url(r'^sesiones/$', 'sesiones_list', name='sesiones_list'),
)
