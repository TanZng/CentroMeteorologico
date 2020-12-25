from django.contrib import admin

# Register your models here.
from climaApp.models import Ciudad, Tarjeta

admin.site.register(Tarjeta)
admin.site.register(Ciudad)
