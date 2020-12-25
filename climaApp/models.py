from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models

from django.contrib.auth.models import User


class Tarjeta(models.Model):
    nombre = models.CharField(
        max_length=200,
        help_text='Ingrese un nombre para la tarjeta (e.g. Mi ciudad)',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ciudad(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
