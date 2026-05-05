from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'), #ruta raiz
    path('contacto/', views.contacto, name='contacto'), #ruta contacto
]