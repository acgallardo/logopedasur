from __future__ import unicode_literals
from datetime import date
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from logopedasur.pacientes.models import Paciente, Direccion_Facturacion


# Create your models here.

@python_2_unicode_compatible
class Factura(models.Model):
    '''
       Model for Invoices table
    '''

    class Meta:
        verbose_name = _('factura')
        verbose_name_plural = _('facturas')

    fecha = models.DateField(_('Fecha'))
    titulo = models.CharField(_(u'titulo'), max_length=255, null=False, blank=True)
    neto = models.DecimalField(_(u'neto'), max_digits=8, decimal_places=2, null=False)
    iva =  models.DecimalField(_(u'iva'), max_digits=5, decimal_places=3)
    bruto = models.DecimalField(_(u'bruto'), max_digits=8, decimal_places=2, null=False)
    pagada = models.BooleanField(_(u'Pagada'), default=False)
    direccion = models.ForeignKey(Direccion_Facturacion, on_delete=models.SET_NULL, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)


    def __str__(self):
        return self.pk + " " + self.titulo
