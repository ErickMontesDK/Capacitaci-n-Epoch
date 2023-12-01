from django.urls import path
from users.views import *
from django.contrib.auth.views import login_required
from users.decorators import administrador_required

urlpatterns = [
    path('', administrador_required(login_required(UserListView.as_view())),name="users_list"),
    path('delete/<int:pk>', administrador_required(login_required(UserDeleteView.as_view())), name='user_delete'),
    path('edit/<int:pk>', administrador_required(login_required(UserUpdateView.as_view())), name='user_edit'),
    path('add/', administrador_required(login_required(UserCreateView.as_view())), name='user_add'),
]
