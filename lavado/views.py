from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

from lavado.models import Articulo, LugarCompra
from lavado.forms import ArticuloForm
from lavado.serializer import ArticuloSerializer, LugaresSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html')

def paquetes(request):
    return render(request, 'paquetes.html')

def articulos_get_all(request):
    articulos = Articulo.objects.select_related('fk_lugar_compra')
    articulos_json = ArticuloSerializer(articulos)
    ## return JsonResponse(, safe=False)
    return  JsonResponse(articulos_json, safe=False)

def articulos_view(request):
    if request.method == 'GET':
        articulos = Articulo.objects.select_related('fk_lugar_compra')
        return render(request, 'articulos_table.html', {'articulos': articulos})

def articulo_create(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            response = form.save()
            return HttpResponseRedirect("/articulos/editar/"+str(response.idarticulo)+"/")
        else:
            return HttpResponse(form.errors)
    else:
        form = ArticuloForm()
        return render(request, 'articulo_nuevo.html', {'form': form})

def articulo_edit(request, id):
    articulo = Articulo.objects.get(pk=id)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        print(form)
        if form.is_valid():
            response = form.save()
            return HttpResponse(response)
        else:
            return HttpResponse(form.errors)
    else:       
        form = ArticuloForm(instance=articulo)
        return render(request, 'articulo_editar.html', {'form': form, 'id':id})

def lugares_get_all(request):
    lugares = LugarCompra.objects.all()
    json_res = LugaresSerializer(lugares)
    ## return JsonResponse(, safe=False)
    return  JsonResponse(json_res, safe=False)