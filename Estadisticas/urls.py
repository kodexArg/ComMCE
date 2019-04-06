from django.urls import path
from . import views

urlpatterns = [
        path('', views.pki),
        path('listado_de_maquinas/', views.ddbb, name='hoja1'),
        path('beneficios/', views.beneficios, name='hoja2'),
]