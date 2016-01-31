from django.contrib import admin

# Register your models here.
from django.contrib import admin
from logopedasur.pacientes.models import Pacientes

# Register your models here.
class PacientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'nif', 'fecha_ingreso')
    search_fields = ('nombre',)
    list_filter = ('nif',)


admin.site.register(Pacientes, PacientesAdmin)
