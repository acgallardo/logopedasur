from django.contrib import admin

from logopedasur.terapeutas.models import Terapeuta, Especialidad
# Register your models here.


# Register your models here.
class TerapeutaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'nif', 'fecha_alta','num_aseguradora',)
    search_fields = ('nombre',)
    list_filter = ('nif',)

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)


admin.site.register(Terapeuta, TerapeutaAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
