from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.
@python_2_unicode_compatible
class Especialidad(models.Model):
    """
       class to enumerate profesionals specialities,
       for example in spanish logopedas, Terapia Ocupacional,
       Psicologa, Maestra Audicion y Lenguaje.
    """
    class Meta:
        verbose_name = _('especialidad')
        verbose_name_plural = _('especialidades')

    nombre = models.CharField(_('nombre'), max_length=255, null=False)

    def __str__(self):
        return self.nombre
@python_2_unicode_compatible
class Terapeuta(models.Model):
    """class to define the table for terapeutas"""
    class Meta:
        verbose_name = _('terapeuta')
        verbose_name_plural = _('terapeutas')

    nombre = models.CharField(_('nombre'), max_length=255, null=False)
    apellidos = models.CharField(_('apellidos'), max_length=255, null=False)
    nif = models.CharField(_('nif'), max_length=9, unique=True)
    fecha_nacimiento = models.DateTimeField(_('Fecha de nacimiento'))
    num_aseguradora = models.CharField(_('num_aseguradora'), max_length=20, null=True)
    fecha_alta = models.DateTimeField(_('Fecha de ingreso'))
    imagen = models.ImageField(upload_to='uploads/', blank=True, null=True)
    telefono = models.CharField(_('telefono'), max_length=12, null=True)
    especialidad = models.ManyToManyField(Especialidad)

    def __str__(self):
        return self.nombre + self.apellidos