from django.contrib import admin

from logopedasur.sesiones.models import Sesion, Sesiontipo

# Register your models here.
class SesionestipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'facturable', 'coste')
    search_fields = ('nombre', 'coste',)
    list_filter = ('nombre', 'coste',)

class SesionesAdmin(admin.ModelAdmin):
    list_display = ('paciente_relacionado', 'tipo_sesion', 'fecha_sesion', 'hora_inicio', 'hora_fin')
    search_fields = ('fecha_sesion', 'pagada')
    list_filter = ('fecha_sesion', 'pagada')

    def paciente_relacionado(self, obj):
        return obj.paciente.nombre + ' ' + obj.paciente.apellidos

    def tipo_sesion(self, obj):
        return obj.tipo.nombre


    paciente_relacionado.short_description = 'Paciente'
    tipo_sesion.short_description = 'Tipo'

admin.site.register(Sesion, SesionesAdmin)
admin.site.register(Sesiontipo, SesionestipoAdmin)
