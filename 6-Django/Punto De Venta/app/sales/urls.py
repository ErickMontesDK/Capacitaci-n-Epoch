from django.urls import path
from sales.views import *


urlpatterns = [
    path('clients/', ClienteListView.as_view(), name='clients_list'),
    path('autocomplete-clients/', autocomplete_Clientes, name='auto_clients'),
    path('autocomplete-products/', autocomplete_Productos, name='auto_products'),
    path('clients/delete/<int:pk>', ClienteDeleteView.as_view(), name='clients_delete'),
    path('clients/add', ClienteCreateView.as_view(), name='clients_add'),
    path('sale/', PantallaVentaView.as_view(), name="pantalla_venta"),
    path('sales_report/', VentaListView.as_view(), name="reporte_ventas"),
    path('sales_report/download', download_excel, name="descargar_excel"),
    path('sales_report/send_mail', send_email, name="send_mail"),
    path('sale/generate_ticket/<int:venta>/', generar_pdf, name="ticket"),
    path('sale/detail_sale/<int:venta>/', DetalleVentaListView.as_view(), name="detalle_venta"),
    path('pdf/<int:venta_id>', pdf_view, name='pdf'),
]
