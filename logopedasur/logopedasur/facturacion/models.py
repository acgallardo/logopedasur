from __future__ import unicode_literals

from decimal import *

from datetime import date
from django.db import models
from django.db.models import Sum, Count
from django.template.defaultfilters import floatformat
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
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion_Facturacion, on_delete=models.SET_NULL, null=True, blank=True)
    neto = models.DecimalField(_(u'neto'), max_digits=8, decimal_places=2, null=True, blank=True)
    tipo_iva =  models.DecimalField(_(u'iva'), max_digits=5, decimal_places=3, null=True, blank=True)
    descuento = models.DecimalField(_(u'descuento'), max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    pagada = models.BooleanField(_(u'Pagada'), default=False)

    def __get_codigo_factura(self):
        '''
            Create -factura- code, concatenate -FACT- with the pk
            with 0 char before pk, until all the code have a size of 9
        '''

        if self.pk < 10:
            return "FACT0000" + str(self.pk)
        elif self.pk < 100:
            return "FACT000" + str(self.pk)
        elif self.pk < 1000:
            return "FACT00" + str(self.pk)
        elif self.pk < 10000:
            return "FACT0" + str(self.pk)
        else:
            return "FACT" + str(self.pk)

    codigo = property(__get_codigo_factura)

    def __get_neto(self):

        query_neto = FacturaDetalle.objects.filter(
            codigo_factura_id=self.pk).aggregate(suma_neto=Sum('total'))
        if query_neto['suma_neto'] == None:
            return 0
        else:
            return format(Decimal(query_neto['suma_neto']), '.2f')

    neto2 = property(__get_neto)


    def __get_cantidad_iva(self):
        '''
            obtain amount of money in taxes (iva)
        '''
        return format(Decimal(self.neto * (self.tipo_iva / 100)),'.2f')
    cantidad_iva = property(__get_cantidad_iva)

    def __get_bruto(self):
        '''
           subtotal = neto + cantidad_iva
        '''
        return format(self.neto + Decimal(self.cantidad_iva),'.2f')
    bruto = property(__get_bruto)

    def __get_total(self):
        cantidad_descuento = Decimal(self.bruto) * (self.descuento/100)
        return format(Decimal(self.bruto) - cantidad_descuento,'.2f')
    total = property(__get_total)

    def __str__(self):
        return str(self.pk) + " " + self.titulo


@python_2_unicode_compatible
class FacturaDetalle(models.Model):
    '''
       Model for Invoices details table
    '''

    class Meta:
        verbose_name = _('Detalle Factura')
        verbose_name_plural = _('Detalles Facturas')

    codigo_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    concepto = models.TextField(_(u'concepto'), null=False, blank=True)
    precio = models.DecimalField(_(u'neto'), max_digits=8, decimal_places=2, null=True, blank=True)
    cantidad = models.DecimalField(_(u'cantidad'), max_digits=6, decimal_places=0, null=True, blank=True)
    sub_total = models.DecimalField(_(u'sub_total'), max_digits=6, decimal_places=0, null=True, blank=True)
    descuento = models.DecimalField(_(u'descuento'), max_digits=5, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(_(u'total'), max_digits=6, decimal_places=0, null=True, blank=True)


    def __str__(self):
        return self.concepto + " " + str(self.total)
