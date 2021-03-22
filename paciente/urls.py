from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_terapia/', views.lista_terapia, name='lista_terapia'),
    path('terapia/', views.terapia, name='terapia'),
    path('nueva_terapia/', views.nueva_terapia, name='nueva_terapia'),
    path('terapia/confirmacion/<int:pk>/', views.confirmacion_terapia, name='confirmacion_terapia'),
    path('terapia/atencion/<int:pk>/', views.terapia_detalle, name='terapia_detalle'),
    path('terapia_anterior/', views.terapia_anterior, name='terapia_anterior'),
    path('eliminar_terapia/<int:pk>', views.eliminar_terapia, name='eliminar_terapia'),
    path('menu/', views.menu, name='menu'),
    path('menu_confirmacion/', views.menu_confirmacion, name='menu_confirmacion'),
    path('campana/', views.campana, name='campana'),
    path('campana_confirmacion/', views.campana_confirmacion, name='campana_confirmacion'),
    path('emergencia/', views.emergencia, name='emergencia'),
    path('transporte/', views.transporte, name='transporte'),
    path('transporte_confirmacion/', views.transporte_confirmacion, name='transporte_confirmacion'),
    path('contacto/', views.contacto, name='contacto'),
    path('accounts/', include('django.contrib.auth.urls')),
]
