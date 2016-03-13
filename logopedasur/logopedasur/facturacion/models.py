from __future__ import unicode_literals

from decimal import *

from datetime import date
from django.db import models
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

    def __get_cantidad_iva(self):
        '''
            obtain amount of money in taxes (iva)
        '''
        return self.neto * (self.tipo_iva / 100)

    cantidad_iva = property(__get_cantidad_iva)

    def __get_bruto(self):
        '''
           subtotal = neto + cantidad_iva
        '''
        return floatformat(Decimal(self.neto) + self.__get_cantidad_iva(),2)

    bruto = property(__get_bruto)

    def __get_total(self):
        cantidad_descuento = float(self.__get_bruto()) * float(self.descuento/100)
        return floatformat(self.__get_bruto() - cantidad_descuento,2)

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
    descuento = models.DecimalField(_(u'descuento'), max_digits=5, decimal_places=2, null=True, blank=True)


    def __get_subtotal(self):
        '''
            Calculate sub_total = precio * cantidad
        '''
        return self.precio * self.cantidad

    sub_total = property(__get_subtotal)

    def __get_total(self):
        '''
            Calculate total = precio * cantidad - %descuento
        '''
        return floatformat(self.__get_subtotal() - (self.__get_subtotal() * (self.descuento/100)),2)

    total = property(__get_total)

    def __str__(self):
        return self.concepto + " " + str(self.total)
