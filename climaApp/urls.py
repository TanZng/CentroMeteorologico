from django.urls import path, reverse_lazy
from . import views

app_name = 'climaApp'
urlpatterns = [
    path('', views.index, name='main'),
    path('tarjetas', views.TarjetaListView.as_view(), name='tarjeta_list'),  # para las templates
    path('tarjeta/<int:pk>/update', views.TarjetaUpdateView.as_view(success_url=reverse_lazy('climaApp:tarjeta_list')), name='tarjeta_update'),
    path('tarjeta/<int:pk>', views.TarjetaDetailView.as_view(), name='tarjeta_detail'), # Este no tiene un template asociado
    path('tarjeta/create', views.TarjetaCreateView.as_view(success_url=reverse_lazy('climaApp:tarjeta_list')), name='tarjeta_create'),
    path('tarjeta/<int:pk>/update', views.TarjetaUpdateView.as_view(success_url=reverse_lazy('climaApp:tarjeta_list')), name='tarjeta_update'),
    path('tarjeta/<int:pk>/delete', views.TarjetaDeleteView.as_view(success_url=reverse_lazy('climaApp:tarjeta_list')), name='tarjeta_delete'),
]
