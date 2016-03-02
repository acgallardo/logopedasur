from datetime import date
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from logopedasur.terapeutas.models import Terapeuta
from logopedasur.pacientes.models import Paciente, Tutor


# Create your models here.
@python_2_unicode_compatible
class Sesiontipo(models.Model):
    '''
        Model for table Sesiontipo where we describe different
        types of session and it's features
    '''

    class Meta:
        verbose_name = _('sesion tipo')
        verbose_name_plural = _('sesiones tipo')

    nombre = models.CharField(_('nombre'), max_length=256,null=False)
    facturable = models.BooleanField(_(u'Facturable'), default=True)
    coste = models.DecimalField(_(u'coste'), max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return self.nombre + " " + str(self.facturable) + " " + str(self.coste)


@python_2_unicode_compatible
class Sesion(models.Model):
    ''' Model for table Sessions'''

    class Meta:
        verbose_name = _('sesion')
        verbose_name_plural = _('sesiones')

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Sesiontipo, on_delete=models.SET_NULL, null=True)
    terapeutas = models.ManyToManyField(Terapeuta)
    fecha_sesion = models.DateField(_('Fecha de sesion'))
    hora_inicio = models.TimeField(_('Hora de inicio'))
    hora_fin = models.TimeField(_('Hora de finalizacion'))
    observaciones = models.TextField(_('observaciones'), blank=True, null=True)


    def __str__(self):
        return self.paciente.nombre + self.paciente.nombre + str(self.fecha_sesion) + str(self.hora_inicio)
