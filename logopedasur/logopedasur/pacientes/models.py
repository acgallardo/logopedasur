from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.
@python_2_unicode_compatible
class Pacientes(models.Model):

    class Meta:
        verbose_name = _('paciente')
        verbose_name_plural = _('pacientes')

    nombre = models.CharField(_('nombre'), max_length=255)
    apellido = models.CharField(_('apellidos'), max_length=255)
    nif = models.CharField(_('nif'), max_length=9)
    fecha_nacimiento = models.DateTimeField(_('Fecha de nacimiento'))
    observaciones = models.TextField(_('observaciones'), blank=True, null=True)

    def __str__(self):
        return self.name + self.apellidos
