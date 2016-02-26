from datetime import date
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from logopedasur.terapeutas.models import Terapeuta

# Create your models here.


@python_2_unicode_compatible
class Paciente(models.Model):
    ''' Model for table Patients'''

    class Meta:
        verbose_name = _('paciente')
        verbose_name_plural = _('pacientes')

    nombre = models.CharField(_('nombre'), max_length=255, null=False)
    apellidos = models.CharField(_('apellidos'), max_length=255, null=False)
    nif = models.CharField(_('nif'), max_length=9, unique=True)
    fecha_nacimiento = models.DateField(_('Fecha de nacimiento'))
    observaciones = models.TextField(_('observaciones'), blank=True, null=True)
    fecha_ingreso = models.DateField(_('Fecha de ingreso'),
                                         default=date.today())
    email = models.EmailField(_('email'), max_length=254, null=True, blank=True)
    telefono = models.CharField(_('telefono'), max_length=12, null=True)
    imagen = models.ImageField(upload_to='uploads/', blank=True, null=True)
    terapeutas = models.ManyToManyField(Terapeuta)

    def __str__(self):
        return self.nombre + self.apellidos

@python_2_unicode_compatible
class Tutor(models.Model):

    class Meta:
        verbose_name = _('tutor')
        verbose_name_plural = _('tutores')

    nombre = models.CharField(_('nombre'), max_length=255, null=False)
    apellidos = models.CharField(_('apellidos'), max_length=255, null=False)
    nif = models.CharField(_('nif'), max_length=9, unique=True)
    email = models.EmailField(_('email'), max_length=254, null=True, blank=True)
    pacientes = models.ManyToManyField(Paciente)

    def __str__(self):
        return self.nombre + self.apellidos


@python_2_unicode_compatible
class Horario(models.Model):

    class Meta:
        verbose_name = _('horario')
        verbose_name_plural = _('horarios')

    DAY_CHOICES = (
        ('LUNES', u'Lunes'),
        ('MARTES', u'Martes'),
        ('MIERCOLES', u'Miercoles'),
        ('JUEVES', u'Jueves'),
        ('VIERNES', u'Viernes'),
        ('SABADO', u'Sabado'),
        ('DOMINGO', u'Domingo'),
    )
    dia = models.CharField(_(u'dia'), max_length=9,
                           choices = DAY_CHOICES,
                           null=False)
    hora_inicio = models.TimeField(_('Hora inicio'), max_length=5, null=False)
    hora_fin = models.TimeField(_('Hora fin'), max_length=5, null=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.dia +' ' + str(self.hora_inicio) + ' ' + str(self.hora_fin)


@python_2_unicode_compatible
class Informe(models.Model):

    class Meta:
        verbose_name = _('informe')
        verbose_name_plural = _('informes')

    INFORME_CHOICES = (
        ('Externo', u'Externo'),
        ('Interno', u'Interno'),
    )
    informe = models.FileField(upload_to='uploads/')
    tipo = models.CharField(_(u'tipo'), max_length=9,
                           choices = INFORME_CHOICES,
                           null=False)
    fecha_informe = models.DateField(_('Fecha de informe'))
    fecha_entrega = models.DateField(_('Fecha de entrega'),
                                         default=date.today())
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tipo + ' ' + str(self.fecha_informe) + ' ' + str(self.paciente.nombre) + ' ' + str(self.terapeuta.nombre)
