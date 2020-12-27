from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .config.remote import baseUrl
import requests
from .models import Tarjeta
from .owner import OwnerCreateView, OwnerListView, OwnerUpdateView, OwnerDetailView, OwnerDeleteView


def index(request):
    if request.user.is_anonymous:
        ciudades = Tarjeta.objects.filter(owner=1)
    else:
        ciudades = Tarjeta.objects.filter(owner=request.user)

    context = getClima(ciudades)
    return render(request, 'climaApp/climaAppMain.html', context)

def getClima(ciudades):
    # lista de ciudades para el contexto
    cl = []

    for ciudad in ciudades:
        apiUrl = baseUrl + str(ciudad.ciudad)
        print(apiUrl)
        # response = requests.get(apiUrl)
        if False:
            print(f)
            #if response.status_code == 200:
            # r = response.json()
            # ciudad_clima = {
            #         'nombre_tarjeta': ciudad.nombre,
            #         'city': r['name'],
            #         'country': r['sys']['country'],
            #         'temperature': r['main']['temp'],
            #         'max': r['main']['temp_max'],
            #         'min': r['main']['temp_min'],
            #         'description': r['weather'][0]['description'],
            #         'viento': r['wind']['speed'],
            #         'humedad': r['main']['humidity'],
            #         'visibilidad': r['visibility'],
            #         'icon': r['weather'][0]['icon'],
            # }
        else:
            ciudad_clima = {
                'nombre_tarjeta': "ERROR AL OBTENER LOS DATOS",
                'city': ciudad.ciudad,
                'country': '404',
                'temperature': '?',
                'max': '?',
                'min': '?',
                'description': 'Error',
                'viento': '?',
                'humedad': '?',
                'visibilidad': '?',
                'icon': '50n',
            }
        cl.append(ciudad_clima)
    context = {'ciudades_list': cl}
    return context

class TarjetaListView(OwnerListView):
    model = Tarjeta
    # By convention:
    # template_name = "ads/ad_list.html"


class TarjetaDetailView(OwnerDetailView):
    model = Tarjeta


class TarjetaCreateView(OwnerCreateView):
    model = Tarjeta
    fields = ['nombre', 'ciudad']


class TarjetaUpdateView(OwnerUpdateView):
    model = Tarjeta
    fields = ['nombre', 'ciudad']


class TarjetaDeleteView(OwnerDeleteView):
    model = Tarjeta
