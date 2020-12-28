from django import forms
from .models import Tarjeta, Ciudad


class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['nombre', 'pais', 'ciudad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['ciudad'].queryset = Ciudad.objects.none()
        if 'pais' in self.data:
            try:
                pais_id = int(self.data.get('pais'))
                self.fields['ciudad'].queryset = Ciudad.objects.filter(pais=pais_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # entrada invalida del cliente; ignorar y poner el conjunto de ciudad en vacío
        elif self.instance.pk:
            self.fields['ciudad'].queryset = self.instance.pais.ciudad_set.order_by('nombre')