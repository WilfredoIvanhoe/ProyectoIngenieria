
def ArticuloSerializer(qs_articulo):
    json_aux = []
    for articulo in qs_articulo:
        aux = {
        'idarticulo' : articulo.idarticulo,
        'nombre' : articulo.nombre,
        'descripcion' : articulo.descripcion,
        'precio' : articulo.precio,
        'cantidad' : articulo.cantidad,
        'codigo_barras' : articulo.codigo_barras,
        'fk_lugar_compra' : articulo.fk_lugar_compra.idlugar_compra,
        'nombre_tienda' : articulo.fk_lugar_compra.nombre_tienda,
        'direccion' : articulo.fk_lugar_compra.direccion,
        }
        json_aux.append(aux.copy())
    return json_aux

def LugaresSerializer(qs_lugares):
    json_aux = []
    for lugar in qs_lugares:
        aux = {
            'id' : lugar.idlugar_compra,
            'nombre' : lugar.nombre_tienda,
            'direccion' : lugar.direccion,
        }
        json_aux.append(aux.copy())
    return json_aux