$(document).ready(function(){
    $( "#cliente" ).autocomplete({
        source: sourceClients,
        select: function(event, ui) {
            const clienteId = ui.item.id;
            
            let eventoCliente = new jQuery.Event("clienteSeleccionado", {detail : clienteId})
            $("#cliente").trigger(eventoCliente)
        }
    });
    $( "#producto" ).autocomplete({
        source: sourceProducts,
        select: function(event, ui) {
            const id = ui.item.id;
            const label = ui.item.label;
            const price = ui.item.precio_unitario;
            const existence = ui.item.existencia;

            let producto = {id, label, price, existence};
            let eventoProducto = new jQuery.Event("productoSeleccionado", producto);

            $("#producto").trigger(eventoProducto)            
        }

    })
})