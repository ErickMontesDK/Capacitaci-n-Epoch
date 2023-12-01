from django.urls import path
from . views import *
from django.contrib.auth.views import login_required
from users.decorators import administrador_required

urlpatterns = [
    path('brands/', administrador_required(login_required(MarcaListView.as_view())), name='marcas'),
    path('brands/delete/<int:pk>',administrador_required(login_required(MarcaDeleteView.as_view())), name='marca_delete'),
    path('brands/add/',administrador_required(login_required(MarcaCreateView.as_view())), name='marca_add'),
    path('brands/update/<int:pk>',administrador_required(login_required(MarcaUpdateView.as_view())), name='marca_update'),
    path('units/', administrador_required(login_required(UnidadMedidaListView.as_view())), name='units_list'),
    path('units/add/', administrador_required(login_required(UnidadMedidaCreateView.as_view())), name='unit_add'),
    path('units/update/<int:pk>',administrador_required(login_required(UnidadMedidaUpdateView.as_view())), name='unit_update'),
    path('units/delete/<int:pk>',administrador_required(login_required(UnidadMedidaDeleteView.as_view())), name='unit_delete'),
    path('departments/', administrador_required(login_required(DepartamentoListView.as_view())), name='departments'),
    path('departments/add/', administrador_required(login_required(DepartamentoCreateView.as_view())), name='department_add'),
    path('departments/update/<int:pk>',administrador_required(login_required(DepartamentoUpdateView.as_view())), name='department_update'),
    path('departments/delete/<int:pk>',DepartamentoDeleteView.as_view(), name='department_delete'),
    path('', administrador_required(login_required(ProductoListView.as_view())), name='products_list'),
    path('add/', administrador_required(login_required(ProductoCreateView.as_view())), name='product_add'),
    path('update/<int:pk>',administrador_required(login_required(ProductoUpdateView.as_view())), name='product_update'),
    path('delete/<int:pk>',administrador_required(login_required(ProductoDeleteView.as_view())), name='product_delete'),

]
