from django.contrib import admin

from logopedasur.sesiones.models import Sesion

# Register your models here.
class SesionesAdmin(admin.ModelAdmin):
    list_display = ('paciente_relacionado','fecha_sesion', 'hora_inicio', 'hora_fin')
    search_fields = ('fecha_sesion',)
    list_filter = ('fecha_sesion',)

    def paciente_relacionado(self, obj):
        return obj.paciente.nombre + ' ' + obj.paciente.apellidos

    paciente_relacionado.short_description = 'Paciente'
admin.site.register(Sesion, SesionesAdmin)
