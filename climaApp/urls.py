import os

from django.conf.urls import url
from django.urls import path, reverse_lazy
from . import views
from django.views.static import serve


app_name = 'climaApp'
urlpatterns = [
    path('', views.index, name='main'),
    path('tarjetas', views.TarjetaListView.as_view(), name='tarjeta_list'),  # para las templates
    path('tarjeta/<int:pk>/update', views.TarjetaUpdateView.as_view(success_url=reverse_lazy('climaApp:tarjeta_list')), name='tarjeta_update'),

    path('tarjeta/<int:pk>', views.TarjetaDetailView.as_view(), name='tarjeta_detail'), # Este no tiene un template asociado

    path('tarjeta/create', views.TarjetaCreateView.as_view(success_url=reverse_lazy('climaApp:tarjeta_list')), name='tarjeta_create'),
    path('tarjeta/<int:pk>/update', views.TarjetaUpdateView.as_view(success_url=reverse_lazy('climaApp:tarjeta_list')), name='tarjeta_update'),
    path('tarjeta/<int:pk>/delete', views.TarjetaDeleteView.as_view(success_url=reverse_lazy('climaApp:tarjeta_list')), name='tarjeta_delete'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # <-- AJAX
]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]
