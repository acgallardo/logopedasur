from django.contrib import admin

# Register your models here.
from django.contrib import admin
from logopedasur.pacientes.models import Pacientes

# Register your models here.
class PacientesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pacientes, PacientesAdmin)
