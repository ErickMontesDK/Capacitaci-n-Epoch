from django.urls import path
from sales.views import *
from django.contrib.auth.views import login_required
from users.decorators import *

urlpatterns = [
    path('clients/', administrador_required(login_required(ClienteListView.as_view())), name='clients_list'),
    path('autocomplete-clients/', login_required(autocomplete_Clientes), name='auto_clients'),
    path('autocomplete-products/', login_required(autocomplete_Productos), name='auto_products'),
    path('clients/delete/<int:pk>', administrador_required(login_required(ClienteDeleteView.as_view())), name='clients_delete'),
    path('clients/add', administrador_required(login_required(ClienteCreateView.as_view())), name='clients_add'),
    path('clients/update/<int:pk>', administrador_required(login_required(ClienteUpdateView.as_view())), name='clients_update'),
    path('sale_screen/', vendedor_required(login_required(PantallaVentaView.as_view())), name="pantalla_venta"),
    path('sales_report/', login_required(VentaListView.as_view()), name="reporte_ventas"),
    path('sales_report/download', login_required(download_excel), name="descargar_excel"),
    path('sales_report/send_mail', send_email, name="send_mail"),
    path('sale/generate_ticket/<int:venta>/', login_required(generar_pdf), name="ticket"),
    path('sale/detail_sale/<int:venta>/', login_required(DetalleVentaListView.as_view()), name="detalle_venta"),
    path('pdf/<int:venta_id>', login_required(pdf_view), name='pdf'),
]
