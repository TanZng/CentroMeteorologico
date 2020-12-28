from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models

from django.contrib.auth.models import User


class Tarjeta(models.Model):
    nombre = models.CharField(
        max_length=50,
        help_text='Ingrese un nombre para la tarjeta (e.g. Mi ciudad)',
        validators=[MinLengthValidator(2, "El nombre debe tener más de 1 carácter")]
    )
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE, null=False)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ciudades"


class Pais(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    iso = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Paises"
