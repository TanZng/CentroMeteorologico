# Url para hacer peticiones, ya incluye la Key de la API
from decouple import config

key = config('API_KEY')
baseUrl = "http://api.openweathermap.org/data/2.5/weather?appid={}&units=metric&lang=es&q=".format(key)
