from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView

from .config.remote import baseUrl, dayUrl
import requests

from .forms import TarjetaForm
from .models import Tarjeta, Ciudad
from .owner import OwnerCreateView, OwnerListView, OwnerUpdateView, OwnerDetailView, OwnerDeleteView


def index(request):
    if request.user.is_anonymous:
        tarjetas = Tarjeta.objects.filter(owner=1)
    else:
        tarjetas = Tarjeta.objects.filter(owner=request.user)

    context = getClima(tarjetas)
    return render(request, 'climaApp/climaAppMain.html', context)


def getClima(tarjetas):
    '''
    Pide a la API el clima de las ciudades recibidas en tarjetas
    :param tarjetas: lista de ciudades
    :return: contexto, con el nombre de la ciudad y toda su información del clima actual
    '''
    # lista de ciudades para el contexto
    cl = []

    for tarjeta in tarjetas:
        apiUrl = baseUrl + str(tarjeta.ciudad) + "," + str(tarjeta.pais.iso)
        #print(apiUrl)
        response = requests.get(apiUrl)
        # if False:
        #     print(f)
        if response.status_code == 200:
            r = response.json()
            ciudad_clima = {
                'nombre_tarjeta': tarjeta.nombre,
                'city': r['name'],
                'country': r['sys']['country'],
                'temperature': r['main']['temp'],
                'max': r['main']['temp_max'],
                'min': r['main']['temp_min'],
                'description': r['weather'][0]['description'],
                'viento': r['wind']['speed'],
                'humedad': r['main']['humidity'],
                'visibilidad': r['visibility'],
                'icon': r['weather'][0]['icon'],
                'id': tarjeta.id,
            }
            # print("HOLA", ciudad_clima)
        else:
            ciudad_clima = {
                'nombre_tarjeta': "ERROR AL OBTENER LOS DATOS",
                'city': tarjeta.ciudad,
                'country': '404',
                'temperature': '?',
                'max': '?',
                'min': '?',
                'description': 'Error',
                'viento': '?',
                'humedad': '?',
                'visibilidad': '?',
                'icon': '50n',
                'id': tarjeta.id,
            }
        cl.append(ciudad_clima)
    context = {'ciudades_list': cl}
    return context

def get_pronostico_api(ciudad, iso):
    '''
    Hace la petición del pronostico de los proximos
    5 días a OpenWeather
    :param ciudad: str ciudad
    :param iso: str iso de un pais (ej MX, US, UK, ...)
    :return: regresa la respuesta json
    '''
    apiUrl = dayUrl + str(ciudad) + "," + str(iso)
    #print(apiUrl)
    response = requests.get(apiUrl)
    return response

class TarjetaListView(OwnerListView):
    model = Tarjeta
    # By convention:
    # template_name = "ads/ad_list.html"


class TarjetaDetailView(DetailView):
    model = Tarjeta
    template_name = "climaApp/tarjeta_detail.html"

    def get(self, request, pk):
        x = Tarjeta.objects.get(id=pk)
        context = self.get_pronostico_semana(x.ciudad, x.pais.iso)
        context['tarjeta'] = x
        return render(request, self.template_name, context)

    def get_pronostico_semana(self, ciudad, iso):
        pronostico = {
            'dias': [],
            'temps': [],
            'vientos': [],
            'humedades': [],
            'visibilidades': []
        }
        response = get_pronostico_api(ciudad, iso)
        if response.status_code == 200:
            r = response.json()
            for i, j in zip(range(0, 40, 8), range(7, 40, 8)):
                #print(f"{i}:{j}")
                self.get_promedio_diario(r['list'][i:j], pronostico)
            # print("HOLA", ciudad_clima)
        return pronostico

    def get_promedio_diario(self, datos, dict):
        '''
        Calcula el clima promedio de un día,
        de n muestras
        :param data: respuesta en json o diccionario
        :param dict:
        :return:
        regresa el promedio de temperatura, visibilidad en dict.
        Regresa True
        '''
        n = len(datos)
        nombre_dia = datos[0]['dt_txt'].split(' ')[0]
        dict['dias'].append(nombre_dia)
        temp = 0
        viento = 0
        humedad = 0
        visibilidad = 0
        # 5 dias cada 3 horas
        # d = data['list']
        # temepratura => d[i]['main']['temp']
        # fecha => d[i]['dt_txt'].split(' ')[0]
        # Viento => d[i]['wind']['speed']
        # Humedad => d[i]['main']['humidity']
        # Visibilidad => d[i]['visibility']
        for dato in datos:
            temp += dato['main']['temp']
            viento += dato['wind']['speed']
            humedad += dato['main']['humidity']
            visibilidad += dato['visibility']
        dict['temps'].append( "{:.2f}".format(temp / n))
        dict['vientos'].append("{:.2f}".format(viento / n))
        dict['humedades'].append("{:.2f}".format(humedad / n))
        dict['visibilidades'].append("{:.2f}".format(visibilidad / n))
        return True

class TarjetaCreateView(OwnerCreateView):
    model = Tarjeta
    form_class = TarjetaForm


class TarjetaUpdateView(OwnerUpdateView):
    model = Tarjeta
    form_class = TarjetaForm


class TarjetaDeleteView(OwnerDeleteView):
    model = Tarjeta


def load_cities(request):
    pais_id = request.GET.get('pais')
    ciudades = Ciudad.objects.filter(pais=pais_id).order_by('nombre')
    # print("CIUDADES: .", ciudades)
    return render(request, 'climaApp/ciudad_dropdown_list_options.html', {'ciudades': ciudades})
