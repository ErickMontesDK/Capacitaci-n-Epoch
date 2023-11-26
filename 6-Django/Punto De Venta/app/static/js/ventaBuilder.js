class VentaBuilder{
    constructor(){
        this.productos = []
        this.subtotal = 0
        this.descuento = 0
        this.total = 0
    }

    addCliente(cliente){
        this.cliente = cliente
        return this
    }
    addVendedor(vendedor){
        this.vendedor = vendedor
        return this
    }
    addProductos(productos){
        this.productos = productos
        return this
    }
    addSubtotal(subtotal){
        this.subtotal = subtotal
        return this
    }
    addDescuento(descuento){
        this.descuento = descuento
        return this
    }
    addTotal(total){
        this.total = total
        return this
    }
    addMetodoPago(metodo){
        this.metodo_pago = metodo
        return this
    }
    addPago_Cliente(pago){
        this.pago = pago
        return this
    }
    addCambio(cambio){
        this.cambio = cambio
        return this
    }
    getCliente(){
        return this.cliente
    }
    getTotal(){
        return this.total
    }
    build(){
        return {
            cliente_id: this.cliente,
            vendedor_id: this.vendedor,
            productos: this.productos,
            subtotal: this.subtotal,
            descuento: this.descuento,
            total: this.total,
            metodo_pago: this.metodo_pago,
            pago: this.pago,
            cambio: this.cambio
        }
    }
}

class ProductoBuilder {
    constructor() {
        this.producto_id = undefined;
        this.cantidad = 1;
        this.precio_unitario = 0;
        this.porcentaje_desc = 0;
    }

    setProducto(id) {
        this.producto_id = id;
        return this;
    }
    setPrecio(precio) {
        this.precio_unitario = precio;
        return this;
    }
    setCantidad(cantidad) {
        this.cantidad = cantidad;
        return this;
    }
    getCantidad(){
        return this.cantidad
    }
    setDescuento(descuento) {
        this.porcentaje_desc = descuento;
        return this;
    }
    build() {
        this.importe = this.cantidad * this.precio_unitario; // Recalcula el importe antes de calcular el total
        this.total = this.importe * (1 - this.porcentaje_desc / 100); // Corregir el cálculo del descuento
        
        return {
            producto: this.producto_id,
            cantidad: this.cantidad,
            precio: this.precio_unitario,
            importe: this.importe,
            descuento: this.porcentaje_desc,
            total: this.total,
        };
    }
}

// let datos = {
//     cliente_id: 5,
//     vendedor_id: 9,
//     productos: [
//         {producto_id: 3, cantidad: 2, precio:150, importe: 300, descuento:10, total:270 },
//         {producto_id: 1, cantidad: 2, precio:150, importe: 300, descuento:10, total:270 },
//         {producto_id: 5, cantidad: 2, precio:150, importe: 300, descuento:10, total:270 },
//     ],
//     subtotal: 900,
//     descuento: 90,
//     total: 810,
//     metodo_pago: 'T',
//     pago: 1000,
//     cambio: 190
// }
// datos.cliente_id = $('#cliente_id').val()
// datos.vendedor_id = $('#vendedor:id').val()






// <!-- datos={
//     cliente : 76,
//     subtotal : 130,
//     descuento : 20,
//     total: 110,
//     productos: [
//         {producto: 12, cantidad: 5, precio_unitario:10, porcentaje_desc: 15%, importe:42.5},
//         {producto: 10, cantidad: 5, precio_unitario:10, porcentaje_desc: 15%, importe:42.5},
//         {producto: 11, cantidad: 5, precio_unitario:10, porcentaje_desc: 15%, importe:42.5},
//         {producto: 9, cantidad: 5, precio_unitario:10, porcentaje_desc: 15%, importe:42.5},
//     ]
// }
//  -->