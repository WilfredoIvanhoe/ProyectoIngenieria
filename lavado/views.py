from django.shortcuts import render
from lavado.forms import ArticuloForm
from django.http import HttpResponse, HttpResponseRedirect
from lavado.models import Articulo
# Create your views here.

def index(request):
    return render(request, 'index.html')

def paquetes(request):
    return render(request, 'paquetes.html')

def articulos_view(request, page):
    print(page)
    if request.method == 'GET':
        idx_1 = (page-1)*4
        idx_2 = page*4
        articulos = Articulo.objects.select_related('fk_lugar_compra').filter(idarticulo__gt=idx_1).filter(idarticulo__lte=idx_2)
        return render(request, 'articulos_table.html', {'articulos': articulos, 'page': page})

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
        if form.is_valid():
            response = form.save()
            return HttpResponse(response)
        else:
            return HttpResponse(form.errors)
    else:       
        form = ArticuloForm(instance=articulo)
        return render(request, 'articulo_editar.html', {'form': form, 'id':id})

        