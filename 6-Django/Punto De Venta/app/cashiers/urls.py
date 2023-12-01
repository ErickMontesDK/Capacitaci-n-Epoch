from django.urls import path
from cashiers.views import *
from django.contrib.auth.views import login_required
from users.decorators import *

urlpatterns = [
    path('catalog/', administrador_required(login_required(CatalogoCajaListView.as_view())), name="cashier_cat_list"),
    path('movements/', administrador_required(login_required(MovimientoCajaListView.as_view())), name="movements_list"),
    path('open_cashier/', vendedor_required(login_required(CatCajaAbrirListView.as_view())), name="open_cashier"),
    path('catalog/add', administrador_required(login_required(CatalogoCajaCreateView.as_view())), name="cashier_cat_add"),
    path('catalog/delete/<int:pk>', administrador_required(login_required(CatalogoCajaDeleteView.as_view())), name="cashier_cat_delete"),
    path('catalog/update/<int:pk>', administrador_required(login_required(CatalogoCajaUpdateView.as_view())), name="cashier_cat_update"),
    path('create_movement/<int:catalogo_id>/', vendedor_required(login_required(MovimientoCajaCreateView.as_view())), name='create_movement'),
    path('close_movement/catalog/<int:catalogo_id>/movement/<int:pk>', vendedor_required(login_required(MovimientoCajaUpdateView.as_view())), name='close_movement'),
]
