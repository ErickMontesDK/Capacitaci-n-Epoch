from django.urls import path
from business.views import *
from django.contrib.auth.views import login_required
from users.decorators import *

urlpatterns = [
    path('',administrador_required(login_required(NegocioCheckView.as_view())), name='status_negocio'),
    path('registrar/',administrador_required(login_required(NegocioCreateView.as_view())), name='registrar_negocio'),
    path('editar/<int:pk>',administrador_required(login_required(NegocioUpdateView.as_view())), name='editar_negocio')
]
