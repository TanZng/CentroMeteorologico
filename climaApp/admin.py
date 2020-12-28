from django.contrib import admin

# Register your models here.
from climaApp.models import Ciudad, Tarjeta, Pais


class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'iso')


class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')


class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'ciudad', 'owner')


admin.site.register(Tarjeta, TarjetaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Pais, PaisAdmin)
