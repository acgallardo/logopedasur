# Register your models here.
from django.contrib import admin

from logopedasur.pacientes.models import Paciente, Tutor, Horario

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


admin.site.register(Paciente, PacientesAdmin)
admin.site.register(Tutor, TutoresAdmin)
admin.site.register(Horario, HorariosAdmin)
