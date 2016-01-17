from django.conf.urls import patterns, url


urlpatterns = patterns(
    'logopedasur.facturacion.views',
    # url (<patron>, funcion, url)
    url(r'^facturas/add/$', 'facturas_add', name='facturas_add'),
    url(r'^facturas/edit/(?P<facturasitem_pk>\d+)/$', 'facturas_edit', name='facturas_edit'),
    url(r'^facturas/$', 'facturas_list', name='facturas_list'),
)
