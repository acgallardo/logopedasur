# Register your models here.
from django.contrib import admin

from logopedasur.pacientes.models import Paciente, Tutor, Horario, Informe, Direccion_Facturacion

# Register your models here.
class PacientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'nif', 'fecha_ingreso')
    search_fields = ('nombre',)
    list_filter = ('nif',)

class TutoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'nif')
    search_fields = ('nombre',)
    list_filter = ('nif',)

class HorariosAdmin(admin.ModelAdmin):
    list_display = ('dia', 'hora_inicio', 'hora_fin')
    search_fields = ('dia','hora_inicio')
    list_filter = ('dia',)

class InformesAdmin(admin.ModelAdmin):
    list_display = ('fecha_informe', 'tipo', 'informe')
    search_fields = ('fecha_informe','tipo')
    list_filter = ('fecha_informe','tipo')

class Direccion_FacturacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'nif', 'direccion', 'localidad', 'cod_postal', 'provincia')
    search_fields = ('nombre_completo', 'nif',)

admin.site.register(Paciente, PacientesAdmin)
admin.site.register(Tutor, TutoresAdmin)
admin.site.register(Horario, HorariosAdmin)
admin.site.register(Informe, InformesAdmin)
admin.site.register(Direccion_Facturacion, Direccion_FacturacionAdmin)
