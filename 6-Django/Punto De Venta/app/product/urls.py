from django.urls import path
from . views import *


urlpatterns = [
    path('brands/', MarcaListView.as_view(), name='marcas'),
    path('brands/delete/<int:pk>',MarcaDeleteView.as_view(), name='marca_delete'),
    path('brands/add/', MarcaCreateView.as_view(), name='marca_add'),
    path('brands/update/<int:pk>',MarcaUpdateView.as_view(), name='marca_update'),
    path('units/', UnidadMedidaListView.as_view(), name='units_list'),
    path('units/add/', UnidadMedidaCreateView.as_view(), name='unit_add'),
    path('units/update/<int:pk>',UnidadMedidaUpdateView.as_view(), name='unit_update'),
    path('units/delete/<int:pk>',UnidadMedidaDeleteView.as_view(), name='unit_delete'),
    path('departments/', DepartamentoListView.as_view(), name='departments'),
    path('departments/add/', DepartamentoCreateView.as_view(), name='department_add'),
    path('departments/update/<int:pk>',DepartamentoUpdateView.as_view(), name='department_update'),
    path('departments/delete/<int:pk>',DepartamentoDeleteView.as_view(), name='department_delete'),
    path('products/', ProductoListView.as_view(), name='products_list'),
    path('products/add/', ProductoCreateView.as_view(), name='product_add'),
    path('products/update/<int:pk>',ProductoUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>',ProductoDeleteView.as_view(), name='product_delete'),

]
