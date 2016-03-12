from django.contrib import admin

from logopedasur.facturacion.models import Factura, FacturaDetalle

# Register your models here.

class FacturasAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'paciente', 'fecha',  'titulo', 'neto', 'iva',
                    'bruto', 'descuento', 'total')
    search_fields = ('codigo', 'fecha', 'titulo', 'paciente',)
    list_filter = ('fecha',)


class FacturasDetalleAdmin(admin.ModelAdmin):
    list_display = ('codigo_factura', 'concepto', 'precio', 'cantidad',
                    'sub_total', 'descuento', 'total')
    search_fields = ('codigo_factura', 'concepto',)
    list_filter = ('codigo_factura',)


admin.site.register(Factura, FacturasAdmin)
admin.site.register(FacturaDetalle, FacturasDetalleAdmin)
