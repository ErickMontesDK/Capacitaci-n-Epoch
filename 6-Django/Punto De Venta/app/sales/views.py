from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, TemplateView, UpdateView
from business.models import Negocio
from cashiers.models import MovimientoCaja
from product.models import Producto
from sales.forms.clients_form import ClienteForm
from sales.models import RAZON_SOCIAL_CHOICES, Cliente, DetalleVenta, Venta
from shared.utils import BaseListView, ContextMixin, getQueryFilterOption
from users.models import User
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import *
from reportlab.lib.units import mm
from reportlab.platypus import *
from reportlab.lib.styles import (ParagraphStyle, getSampleStyleSheet)
from reportlab.lib import colors
import django_excel as excel
from django.conf import settings
from django.core.mail import EmailMessage

class ClienteListView(BaseListView):
    model = Cliente
    template_name = 'clientes_list.html'
    template_render = 'clientes_table.html'
    title = 'Clientes'
    subtitle = 'Lista de clientes registrados'
    filter_range = ['id', 'nombre','apellido','telefono','email','rfc','razon_social','direccion']
    add_element_url = reverse_lazy('clients_add')
    list_url = reverse_lazy('clients_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["razones_sociales"] = RAZON_SOCIAL_CHOICES 
        return context

class ClienteDeleteView(ContextMixin, DeleteView):
    model = Cliente
    template_name = "delete_record.html"
    success_url = reverse_lazy("clients_list")
    title = "Borrar cliente"
    subtitle = f"Eliminar registros de cliente"
    list_name = "Clientes"
    list_url = reverse_lazy('clients_list') 

    
class ClienteCreateView(ContextMixin, CreateView):
    model = Cliente
    template_name = "clients_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy('clients_list')
    title = "Nuevo cliente"
    subtitle = "Agregar nuevo registro de cliente"
    list_name = "Clientes"
    list_url = reverse_lazy('clients_list')
    
class ClienteUpdateView(ContextMixin, UpdateView):
    model = Cliente
    template_name = "clients_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy('clients_list')
    title = "Editar Cliente"
    subtitle = "Editar registro de cliente"
    list_name = "Clientes"
    list_url = reverse_lazy('clients_list')
    
    
class PantallaVentaView(TemplateView):
    template_name = "pantalla_venta.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pantalla de Venta" 
        context['subtitle'] = ""
        context['base_url'] = reverse_lazy('pantalla_venta')
        return context
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        try:
            REGISTRO_VENTA = self.request.POST
            cliente = Cliente.objects.get(pk=REGISTRO_VENTA["cliente_id"])
            seller = User.objects.get(pk=REGISTRO_VENTA['vendedor_id']) 
            movimiento_de_compra = seller.get_movimiento_caja()
            movimiento_de_compra.entrada_efectivo = movimiento_de_compra.entrada_efectivo + Decimal(REGISTRO_VENTA['total'])
            movimiento_de_compra.save()
            
            productos = []
            existIndex = True
            index = 0
            while existIndex:
                producto = {}
                keys = [key for key in REGISTRO_VENTA if key.startswith(f'productos[{index}][')]
                
                if len(keys)>0:
                    for key in keys:
                        value = REGISTRO_VENTA[f'{key}']
                        key_lenght = len(f'productos[{index}][')
                        new_key = key[key_lenght:][:-1]
                        
                        producto[f'{new_key}'] = value
                    productos.append(producto)
                    index += 1
                else : 
                    existIndex = False            
            
            venta = Venta.objects.create(
                cliente=cliente,
                movimiento_caja = movimiento_de_compra,
                metodo_pago = REGISTRO_VENTA['metodo_pago'],
                subtotal=REGISTRO_VENTA['subtotal'],
                descuento=REGISTRO_VENTA['descuento'],
                total=REGISTRO_VENTA['total'],
                monto=REGISTRO_VENTA['pago'],
                vuelto=REGISTRO_VENTA['cambio'])
            
            lista_productos = [(producto['producto'], producto['cantidad'],producto['importe'],producto['descuento'],producto['total']) for producto in productos]
            for id, cantidad, importe, descuento, total in lista_productos:
                                
                productoRecord = Producto.objects.get(pk=id)
                
                detalle_venta = DetalleVenta.objects.create(
                    cantidad_prod = cantidad,
                    importe = importe,
                    descuento = descuento, 
                    total = total,
                    producto = productoRecord,
                    venta = venta 
                )
                
                productoRecord.existencia = F('existencia') - cantidad
                productoRecord.save()
                url_ticket = reverse_lazy('ticket', kwargs={'venta': venta.id})
                        
            return JsonResponse({"message": "Venta registrada correctamente",'ticket':url_ticket}, status=201)
        except Exception as e:
            return JsonResponse({"message": "Ocurrió un error al registrar la venta", "error": str(e)}, status=400)
            
    
    
def autocomplete_Clientes(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        query = request.GET.get('term', '')
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query)
        )
        results = [{'id': cliente.id, 'label': f"{cliente.nombre} {cliente.apellido}"} for cliente in clientes]
        
        return JsonResponse(results, safe=False)
    
def autocomplete_Productos(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        query = request.GET.get('term', '')
        productos = Producto.objects.filter(existencia__gt=0).filter(nombre__icontains=query)
        
        results = [{'id': producto.id, 'label': f"{producto.nombre}", 'precio_unitario':producto.precio_unitario, 'existencia':producto.existencia} for producto in productos]
        
        return JsonResponse(results, safe=False)

def generar_pdf(request, venta):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="ticket.pdf"'
    page_size = (74*mm, 2*mm)
    p = canvas.Canvas(response, pagesize=page_size)
    
    venta_obj = get_object_or_404(Venta, pk=venta)
    cliente = venta_obj.cliente
    detalles_venta = DetalleVenta.objects.filter(venta = venta_obj)
    negocio = Negocio.objects.first() if Negocio.objects.exists() else {}  
        
    informaciónNegocio = (
        f"Dirección: {negocio.direccion}"
        "<br/>"
        "Unidad: 001. "
        f"Teléfono: {negocio.telefono}. "
        f"E-mail: {negocio.email}"
    )
    msg = f"""
    ¿Comó te atendimos?<br/>
    ¿Necesitas ayuda ahora?<br/>
    {negocio.telefono}<br/>
    ---------------------------<br/>
    ¡Gracias por tu compra!<br/>
    ---------------------------<br/>
    {venta_obj.fecha.strftime("%d/%m/%y %H:%M")}
    """
    
    informacionCliente = (
        f"Cliente: {cliente.nombre} {cliente.apellido}. "
        f"Tel: {cliente.telefono}. <br/>"
        f"E-mail:, {cliente.email}. "
        f"R.F.C: {cliente.rfc}. "
        f"Razón social: {cliente.razon_social}. "
    )
    
    productos = [
        ["Clave","Producto","Cant","Importe","Descuento"],
    ]
    articulos_vendidos = 0
    
    for detalle_venta in detalles_venta:
        producto = [
            detalle_venta.producto.id,
            detalle_venta.producto.nombre[:13],
            detalle_venta.cantidad_prod,
            detalle_venta.importe,
            -round(((detalle_venta.descuento/100)*detalle_venta.importe),2)
        ]
        articulos_vendidos += detalle_venta.cantidad_prod
        productos.append(producto)
        
    resumenCompra = [
        ['Artículos vendidos',f"{articulos_vendidos}"],
        ["Subtotal",f"${venta_obj.subtotal}"],
        ["Descuento",f"${venta_obj.descuento}"],
        ["Total",f"${venta_obj.total}"],
        ["Efectivo",f"${venta_obj.monto}"],
        ["Cambio",f"${venta_obj.vuelto}"],
        ["Método de pago",f"{venta_obj.metodo_pago.capitalize()}"]
    ]
    
    paragraphStyle = ParagraphStyle(name="Estilo",
                                fontSize = 8,
                                alignment = 1,
                                leading=11
                                )
    tableStyle = TableStyle([
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"), 
                        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"), 
                        ("FONTSIZE", (0, 0), (-1, -1), 8),
                        ("SPLITBYROWSPAN", (0, 0), (-1, -1), True),
                        ("TOPPADDING", (0, 0), (-1, -1), 1),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                    ])
    
    paragraph = Paragraph(informaciónNegocio, style=paragraphStyle)
    paragraphClient = Paragraph(informacionCliente, style=paragraphStyle)
    paragraphMsg = Paragraph(msg, style=paragraphStyle)
    productosTabla = Table(productos, colWidths=[20, 70, 20, 40, 40])
    resumenTabla = Table(resumenCompra)
    productosTabla.setStyle(tableStyle)
    resumenTabla.setStyle(tableStyle)
    
    altura_total = page_size[1]
    title_text = f"{negocio.nombre}"
    title_height = 6*mm
    
    paragraph.wrapOn(p, page_size[0], page_size[1])
    infoParagraph = paragraph.height + 2*mm
    paragraphClient.wrapOn(p, page_size[0], page_size[1])
    clientParagraphHeight = paragraphClient.height + 2*mm
    productosTabla.wrapOn(p, page_size[0], page_size[1])
    ancho_tabla, alto_tabla = productosTabla.wrapOn(p, page_size[0], page_size[1])
    productosTablaHeight = alto_tabla + 2*mm
    lineaSeparacionHeight = 1*mm
    anchoResumen, alto_resumen = resumenTabla.wrapOn(p, page_size[0], page_size[1])
    resumenTablaHeight = alto_resumen + 2*mm
    paragraphMsg.wrapOn(p, page_size[0], page_size[1])
    mensajeHeight = paragraphMsg.height + 2*mm
    
    altura_total += title_height + infoParagraph + clientParagraphHeight + productosTablaHeight + 2*lineaSeparacionHeight + resumenTablaHeight + mensajeHeight

    title_width = p.stringWidth(title_text, 'Helvetica', 12)
    
    page_size = (74*mm, altura_total)
    p = canvas.Canvas(response, pagesize=page_size)
    alturaAcumulada = altura_total - title_height
    title = p.beginText((page_size[0] - title_width) / 2, alturaAcumulada)
    title.setFont("Helvetica", 12)
    title.textLine(title_text)
    p.drawText(title)
    alturaAcumulada -= infoParagraph
    paragraph.drawOn(p, (page_size[0] - paragraph.width) / 2, alturaAcumulada)
    alturaAcumulada -= clientParagraphHeight
    paragraphClient.drawOn(p, (page_size[0] - paragraphClient.width) / 2, alturaAcumulada)
    alturaAcumulada -= productosTablaHeight
    x = (page_size[0] - ancho_tabla) / 2
    productosTabla.drawOn(p, x, alturaAcumulada)
    alturaAcumulada -= lineaSeparacionHeight
    p.line(0, alturaAcumulada, page_size[0], alturaAcumulada)
    alturaAcumulada -= resumenTablaHeight
    resumenTabla.drawOn(p, 20, alturaAcumulada)
    alturaAcumulada -= lineaSeparacionHeight
    p.line(0, alturaAcumulada, page_size[0], alturaAcumulada)
    alturaAcumulada -= mensajeHeight
    paragraphMsg.drawOn(p, (page_size[0] - paragraphMsg.width) / 2, alturaAcumulada)
    
    p.setTitle(f'Ticket de compra')
    p.showPage()
    p.save()
    return response

class VentaListView(BaseListView):
    model = Venta
    template_name = 'ventas_list.html'
    template_render = 'ventas_table.html'
    title = 'Reporte de ventas'
    subtitle = 'Registros de ventas'
    filter_range = ['id','cliente','movimiento_caja','fecha','total']
    add_element_url = reverse_lazy('product_add')
    list_url = reverse_lazy('reporte_ventas')
    hideAddElement = True
    
    def get_queryset(self):
        page = int(self.request.GET.get('page', 1))
        orderBy = self.request.GET.get('orderBy', 'id')
        campos = self.request.GET
        
        filters, condicionalOr = getQueryFilterOption(campos)
        user = self.user
        if user.rol == "vendedor":
            query = ListView.get_queryset(self).filter(movimiento_caja__vendedor_encargado__id=user.id).filter(**filters).filter(condicionalOr).order_by(orderBy)
        else:
            query = ListView.get_queryset(self).filter(**filters).filter(condicionalOr).order_by(orderBy)
        
        page_size = 10
        pagination = Paginator(query, page_size, 0, True)
        page = pagination.page(page)
        return page, query.count()
    
    
class DetalleVentaListView(TemplateView):
    template_name = "detalle_venta.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detalle de venta" 
        context['subtitle'] = f"Reporte de venta clave #{self.venta.id}"
        context['base_url'] = reverse_lazy('reporte_ventas')
        context['venta'] = self.venta
        context['cliente'] = self.cliente
        context['detalles_venta'] = self.detalles_venta
        
        if Negocio.objects.exists():
            context['negocio'] = Negocio.objects.first()
        return context
    
    def dispatch(self, request, *args, **kwargs):
        venta_id = self.kwargs.get('venta')
        self.venta = get_object_or_404(Venta, id=venta_id)
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,*args,**kwargs):
        self.detalles_venta = DetalleVenta.objects.filter(venta=self.venta)
        self.movimiento_caja = get_object_or_404(MovimientoCaja, id=self.venta.movimiento_caja.id)
        self.cliente = get_object_or_404(Cliente, id=self.venta.cliente.id)
        self.vendedor = get_object_or_404(User, id=self.movimiento_caja.vendedor_encargado.id)
        
        return super().get(request, *args, **kwargs)
    
    def obtener_contexto_pdf(self):
        return {
            'venta': self.venta,
            'cliente': self.cliente,
            'detalles_venta': self.detalles_venta,
            'movimiento_caja': self.movimiento_caja,
            'vendedor': self.vendedor
        }
    

def pdf_view(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    cliente = get_object_or_404(Cliente, id=venta.cliente.id)
    detalles_venta = DetalleVenta.objects.filter(venta=venta)
    negocio = Negocio.objects.first() if Negocio.objects.exists() else {}  

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="detalle_venta_{venta_id}.pdf"'
    page_size = letter

    p = canvas.Canvas(response, pagesize=page_size)

    p.setFont("Helvetica-Bold", 14)

    p.drawString(50, 750, "Detalle de Venta")
    p.drawString(400, 750, f"{negocio.nombre}")
    p.setFont("Helvetica", 10)
    
    informacionNeg = Paragraph(f"{negocio.direccion}")
    informacionNeg.wrapOn(p,45*mm,1000)
    y_position = 740-informacionNeg.height
    informacionNeg.drawOn(p,400,y_position)
    
    contactoNeg = Paragraph(f"{negocio.email}, {negocio.telefono}")
    contactoNeg.wrapOn(p,45*mm,1000)
    y_position -= contactoNeg.height
    contactoNeg.drawOn(p,400,y_position)
    
    y_position -= 20
    p.drawString(50, y_position, f"Estimad@ {cliente} ({cliente.email if cliente.email else 'Sin definir'})")
    p.setFillColor(colors.gray)
    y_position -= 20
    p.drawString(50, y_position, "Aquí están sus detalles de compra. Gracias por su compra.")
    p.setFillColor(colors.black)
    y_position -= 10
    p.line(0,620,page_size[0],620)

    y_position -= 20 
    
    facturacionStyle = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.gray),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ])
    
    datos_facturacion = [
        ['ID de Venta', 'Fecha y hora', 'Razón social', 'Dirección de facturación'],
        [venta.id,
        venta.fecha.strftime('%d de %m del %Y a las %H:%M'), 
        cliente.razon_social if cliente.razon_social else 'Sin definir',
        cliente.direccion if cliente.direccion else 'Sin definir']
        ]
    
    facturacion_table = Table(datos_facturacion, colWidths=[50, 200,140,140])
    facturacion_table.setStyle(facturacionStyle)
    ancho_tabla, alto_tabla = facturacion_table.wrapOn(p,page_size[0],page_size[1])
    y_position -= alto_tabla
    
    facturacion_table.drawOn(p,50,y_position)

    data = [["Clave", "Producto", "Cantidad", "Importe", "Descuento"]]

    for detalle in detalles_venta:
        data.append([
            str(detalle.producto.id),
            str(detalle.producto),
            str(detalle.cantidad_prod),
            f"${detalle.importe}",
            f"{detalle.descuento}%"
        ])


    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
    ])

    y_position -= 20
    tamaño_tabla_disponible = y_position-50
    
    new_data = []
    previous_table = None
    previous_width, previous_height = 0, 0
    
    
    productos_table = Table(data, colWidths=[40,250,60,70,70], splitByRow=True,repeatRows=1)
    productos_table.setStyle(style)
    partes = productos_table.split(400, tamaño_tabla_disponible)
    
    if partes==[]:
        partes.append(productos_table)
    
    ancho, alto = partes[0].wrapOn(p, 400, tamaño_tabla_disponible)
    y_position -= alto
    partes[0].drawOn(p, 50, y_position)
    
    if (y_position-20)>50:
        y_position = y_position-20 
    else: 
        y_position = page_size[1]-50
        p.showPage()
    
    if(len(partes)>1):
        partes = partes[1:]
        lista_restante = []
        
        for i in range(0, len(partes)):
            
            if i==0:
                lista_restante = partes[i]._cellvalues
            else:
                lista_restante.extend(partes[i]._cellvalues[1:]) 
                
        productos_table = Table(lista_restante, colWidths=[40,250,60,70,70], splitByRow=True,repeatRows=1)
        productos_table.setStyle(style)
        partes = productos_table.split(400, page_size[1])
        
        for indice,parte in enumerate(partes):
            y_position = page_size[1]-50
            ancho, alto = parte.wrapOn(p, 400, page_size[1])
            y_position -= alto
            parte.drawOn(p, 50, y_position)
            
            if indice == len(partes) - 1:
                if y_position < 70:
                    p.showPage()
                else:
                    y_position -= 20
            else:
                p.showPage()

        
        
        
        
    # print(partes[0])
    
    # for i in range(0,len(data)):
        
    #     new_data.append(data[i])
            
    #     productos_table = Table(new_data, colWidths=[40,250,60,70,70], splitByRow=True,repeatRows=1)
    #     productos_table.setStyle(style)
    #     ancho_tabla, altura_tabla = productos_table.wrapOn(p, 400, tamaño_tabla_disponible)
        
    #     #Cabe la tabla sin dividir página
    #     if data == new_data and (y_position - altura_tabla) > 50:
    #         y_position -= altura_tabla
    #         productos_table.drawOn(p, 50, y_position)
            
    #     #No cabe toda la tabla, hay que dividirla
    #     elif y_position < altura_tabla:
    #         previous_table.drawOn(p, 50, y_position- previous_height)
    #         p.showPage()
    #         y_position = page_size[1]-50
            
    #         new_data = data[0:1]
    #         new_data.append(data[i])
    #         tamaño_tabla_disponible = page_size[1]
    #     elif i == len(data)-1 and y_position > altura_tabla: 
    #         y_position -= altura_tabla
    #         productos_table.drawOn(p, 50, y_position)
            
    #     previous_table = productos_table
    #     previous_width, previous_height = ancho_tabla, altura_tabla
        
    # y_position -= 50
    # p.drawString(400, y_position, f"Subtotal: ${venta.subtotal}")
    # y_position -= 20
    # p.drawString(400, y_position, f"Descuento: ${venta.descuento}")
    # y_position -= 20
    # p.setFont("Helvetica-Bold", 12)
    # p.drawString(400, y_position, f"Total: ${venta.total}")
    # p.setFont("Helvetica", 12)
    # y_position -= 20
    # p.drawString(400, y_position, f"Método de pago: {venta.metodo_pago.capitalize()}")
    p.setFont("Helvetica", 12)
    estilos = getSampleStyleSheet()
    resumen = [
        f"Subtotal: ${venta.subtotal}",
        f"Descuento: ${venta.descuento}",
        f"<b>Total: ${venta.total}</b>",  # Usa etiquetas HTML para texto en negrita
        f"Método de pago: {venta.metodo_pago.capitalize()}"
    ]
    style = ParagraphStyle("estilo", 
            parent=estilos["BodyText"],
            fontSize = 11,
            )

    resumenPara = Paragraph("<br/><br/>".join(resumen), style)
    resumenPara.wrapOn(p, 55*mm, page_size[1] )
    
    if y_position - resumenPara.height < 50:
        p.showPage()
        y_position = page_size[1]-50
        
    resumenPara.drawOn(p, 400, y_position-resumenPara.height)

    # Guardar el PDF
    p.setTitle(f'Factura de compra')
    p.showPage()
    p.save()

    return response

def download_excel(request):
    orderBy = request.GET.get('orderBy', 'id')
    campos = request.GET
    filters, condicionalOr = getQueryFilterOption(campos)
    
    query = Venta.objects.filter(**filters).filter(condicionalOr).order_by(orderBy)
    print(query.query)
    excel_data = []
    VentaFields = [{'name': 'id', 'type': 'BigAutoField', 'choices': None}, {'name': 'cliente', 'type': 'ForeignKey', 'choices': None}, {'name': 'movimiento_caja', 'type': 'ForeignKey', 'choices': None}, {'name': 'fecha', 'type': 'DateTimeField', 'choices': None}, {'name': 'total', 'type': 'DecimalField', 'choices': None}]
    excel_data.append([field.get('name').capitalize() for field in VentaFields ])
    for record in query:
        item = []
        for field in VentaFields:
            if field.get('type','') == 'ForeignKey':
                item.append(getattr(record, field.get('name')).__str__())
            elif field.get('type',"") == 'DateTimeField':
                item.append(getattr(record, field.get('name')).strftime("%d/%m/%Y %H:%M"))    
            else: 
                item.append(getattr(record, field.get('name')))
        excel_data.append(item)
                
    sheet = excel.pe.Sheet(excel_data)
    return excel.make_response(sheet, "xlsx", 200,"reporte de ventas")

def send_email(request):
    try:
        venta_id = request.GET.get('venta_id',None)
        venta = get_object_or_404(Venta, id=venta_id)
        cliente = get_object_or_404(Cliente, id=venta.cliente.id)
        emailToSend = cliente.email
        pdf_content = pdf_view(request, venta_id)
        
        email = EmailMessage(
            'Detalle de venta',
            f'''Estimado {cliente.nombre_completo()}:
            
Le adjuntamos en este correo un archivo pdf con los detalles de su compra.
            
Sin más, esperamos verl@ pronto. ''',
            settings.EMAIL_HOST_USER,
            [f'{emailToSend}'], 
        )
        email.attach(f'detalle_venta_{venta_id}.pdf', pdf_content.getvalue(), 'application/pdf')
        email.send()
        
        return JsonResponse({'msg':f'Se ha enviado un correo a {cliente.nombre_completo()}.'}, status=201)
    except:
        return JsonResponse({'msg':f'No se envió el email al correo {cliente.nombre_completo()}.'}, status=400)