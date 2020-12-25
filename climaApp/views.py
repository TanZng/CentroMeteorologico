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
        #apiUrl = baseUrl + str(ciudad.ciudad)
        #print(apiUrl)
        # response = requests.get(apiUrl)
        # if response == 401:
        #     r = response.json()
        #     ciudad_clima = {
        #         'city': r['name'],
        #         'country': r['sys']['country'],
        #         'temperature': r['main']['temp'],
        #         'description': r['weather'][0]['description'],
        #         'icon': r['weather'][0]['icon'],
        #     }
        ciudad_clima = {
            'nombre_tarjeta': ciudad.nombre,
            'city': ciudad.ciudad,
            'country': 'US',
            'temperature': '12',
            'description': 'muy nuboso',
            'icon': '04n',
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
