var lugares = [];
var changesQueue = [];
var csrf_token = $('input[name^="csrfmiddlewaretoken"]').val();
var table = new Tabulator("#articulos-table", {
    height:"311px",
    layout:"fitData",
    index: "idarticulo",
    reactiveData:true,
    persistence:true,
    placeholder: "Los datos no han podido ser cargados.",
    rowUpdated:function(row){
        //row - row component
        changesQueue.push(row._row.data)
        updateLastQueue()
    },
    columns:[
        {title:"Id", field: "idarticulo", visible:false},
        {title:"Nombre", field:"nombre", sorter:"string", width:150, editor:"input", 
        cellEdited:callUpdateData},
        {title:"Descripción", field:"descripcion", sorter:"string", width: 200, editor:"input"},
        {title:"Precio", field:"precio", sorter:"number", width:100, editor:"number"},
        {title:"Cantidad", field:"cantidad", sorter:"number", width:100, editor:"number"},
        {title:"IdLugar", field: "fk_lugar_compra", visible:false},
        {title:"Lugar de compra", field:"nombre_tienda", sorter:"string", editor:"select",
            editorParams: function(cell){
                var val = [];
                lugares.forEach(function(lugar){
                    val.push({label: lugar.nombre, value: lugar.id})
                });
                return {values: val};
            },
            cellEdited:function(cell_obj){
                //data - the updated table data
                var cell = cell_obj._cell
                var row = cell.row.data
                var fk_lugar = cell.value
                row.fk_lugar_compra = fk_lugar;
                row.nombre_tienda = lugares.find(element => element.id == fk_lugar).nombre;
                row.direccion = lugares.find(element => element.id == fk_lugar).direccion;
                console.log(row)
                table.updateData([row])
            },                
        },
        {title:"Dirección", field:"direccion", sorter:"string", editor:"input"},
    ]
});
const getLugares = new Promise((resolve, reject) => {
    $.ajax({
        url: "/lugares/get/all/",
        type: 'GET',
        data: {},
        success: function(data) {
        resolve(data)
        },
        error: function(error) {
        reject(error)
        },
    });
});
function callUpdateData(cell_obj){
    var cell = cell_obj._cell
    var row = cell.row.data
    table.updateData([row])
};
function sendUpdates(articulo, id){
    $.ajax({
		url : '/articulos/editar/'+String(id)+'/',
		type: 'post',
		data : articulo
	}).done(function(response){ //
		alert('Bien');
	}).fail(function(data){
        console.log('nuu')
    });
}
function updateLastQueue(){
    var data = changesQueue.pop();
    var id = data.idarticulo;
    var articulo = {
        csrfmiddlewaretoken: csrf_token,
        id: data.idarticulo,
        nombre :  data.nombre,
        descripcion : data.descripcion,
        precio : data.precio,
        cantidad : data.cantidad,
        codigo_barras : '',
        fk_lugar_compra : data.fk_lugar_compra
    }
    sendUpdates(articulo, id);
}
// Document-Ready
$( document ).ready(function() {

    getLugares.then(data => {
        lugares = data
    }).catch(error => {
        console.log(error)
    })
    table.setData("/articulos/get/all/")
});