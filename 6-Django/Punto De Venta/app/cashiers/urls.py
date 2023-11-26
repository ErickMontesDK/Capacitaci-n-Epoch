from django.urls import path
from cashiers.views import *


urlpatterns = [
    path('catalog/', CatalogoCajaListView.as_view(), name="cashier_cat_list"),
    path('movements/', MovimientoCajaListView.as_view(), name="movements_list"),
    path('open_cashier/', CatCajaAbrirListView.as_view(), name="open_cashier"),
    path('catalog/add', CatalogoCajaCreateView.as_view(), name="cashier_cat_add"),
    path('catalog/delete/<int:pk>', CatalogoCajaDeleteView.as_view(), name="cashier_cat_delete"),
    path('catalog/update/<int:pk>', CatalogoCajaUpdateView.as_view(), name="cashier_cat_update"),
    path('create_movement/<int:catalogo_id>/', MovimientoCajaCreateView.as_view(), name='create_movement'),
    path('close_movement/catalog/<int:catalogo_id>/movement/<int:pk>', MovimientoCajaUpdateView.as_view(), name='close_movement'),
]
