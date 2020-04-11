from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paquetes/', views.paquetes, name="paquetes"),
    path('articulos/nuevo/', views.articulo_create, name="Nuevo Articulo"),
    path('articulos/editar/<int:id>/', views.articulo_edit, name="Editar Articulo"),
    path('articulos/editar/', views.articulo_edit, name="Articulo Editado"),
    path('articulos/', views.articulos_view, name="Articulos"),
    path('articulos/get/all/', views.articulos_get_all, name="Articulos all"),

    path('lugares/get/all/', views.lugares_get_all, name="Lugares all"),
]
