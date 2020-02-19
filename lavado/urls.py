from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name="index"),
    path('paquetes', views.paquetes, name="paquetes"),
    path('dashboard', views.dashboard, name="dashboard"),

]
