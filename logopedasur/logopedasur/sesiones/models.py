from datetime import date
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from logopedasur.terapeutas.models import Terapeuta
from logopedasur.pacientes.models import Paciente, Tutor


# Create your models here.


@python_2_unicode_compatible
class Sesion(models.Model):
    ''' Model for table Sessions'''

    class Meta:
        verbose_name = _('sesion')
        verbose_name_plural = _('sesiones')

    TIPO_SESIONES_CHOICES = (
        ('Entrevista', u'Entrevista'),
        ('Sesion30', u'Sesion 30 minutos'),
        ('Sesion45', u'Sesion 45 minutos'),
    )
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    terapeutas = models.ManyToManyField(Terapeuta)
    fecha_sesion = models.DateField(_('Fecha de sesion'))
    hora_inicio = models.TimeField(_('Hora de inicio'))
    hora_fin = models.TimeField(_('Hora de finalizacion'))
    tipo = models.CharField(_(u'tipo'), max_length=15,
                           choices = TIPO_SESIONES_CHOICES,
                           null=True)
    facturable = models.BooleanField(_(u'Facturable'), default=True)
    observaciones = models.TextField(_('observaciones'), blank=True, null=True)


    def __str__(self):
        return self.paciente.nombre + self.paciente.nombre + str(self.fecha_sesion) + str(self.hora_inicio)
