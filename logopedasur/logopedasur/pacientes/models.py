from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.
@python_2_unicode_compatible
class Pacientes(models.Model):

    class Meta:
        verbose_name = _('paciente')
        verbose_name_plural = _('pacientes')

    nombre = models.CharField(_('nombre'), max_length=255, null=False)
    apellidos = models.CharField(_('apellidos'), max_length=255, null=False)
    nif = models.CharField(_('nif'), max_length=9, unique=True)
    fecha_nacimiento = models.DateTimeField(_('Fecha de nacimiento'))
    observaciones = models.TextField(_('observaciones'), blank=True, null=True)
    fecha_ingreso = models.DateTimeField(_('Fecha de ingreso'), auto_now_add=True)


    def __str__(self):
        return self.nombre + self.apellidos


class tutor(models.Model):

    class Meta:
        verbose_name = _('tutor')
        verbose_name_plural = _('tutores')

    nombre = models.CharField(_('nombre'), max_length=255, null=False)
    apellidos = models.CharField(_('apellidos'), max_length=255, null=False)
    nif = models.CharField(_('nif'), max_length=9, unique=True)

    def __str__(self):
        return self.nombre + self.apellidos
