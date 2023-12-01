from django.forms.models import BaseModelForm
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from users.forms.users_form import UserForm
from shared.utils import BaseListView, getQueryFilterOption
from users.models import User
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password


class UserListView(BaseListView):
    model = User
    template_name = 'user_list.html'
    template_render = 'user_table.html'
    title = 'Usuarios'
    subtitle = 'Lista de usuarios registradas'
    filter_range = ['id','username','first_name','last_name','email','rol','genero']
    add_element_url = reverse_lazy('user_add')
    list_url = reverse_lazy('users_list')
    
    
class UserDeleteView(DeleteView):
    model = User
    template_name = "delete_record.html"
    success_url = reverse_lazy('users_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Borrar usuario" 
        context['subtitle'] = f"Eliminar '{self.object}' de registros de usuarios"
        context['list_url'] = reverse_lazy('users_list')
        context['list'] = "Usuarios"
        context['entity'] = 'usuario'
        return context

class UserCreateView(CreateView):
    model = User
    template_name = "user_form.html"
    form_class = UserForm
    success_url = reverse_lazy('users_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nuevo usuario" 
        context['subtitle'] = "Agregar nuevo registro de usuario"
        context['list_url'] = reverse_lazy('users_list')
        context['list'] = "Usuarios"
        return context
    
    def form_valid(self, form):
        usuario = form.instance
        password = form.cleaned_data['password']
        if 'image' in self.request.FILES:
            form.instance.image = self.request.FILES['image']
        if password:
            usuario.password = make_password(password)
        else:
            usuario.password = usuario.password
        return super().form_valid(form)
    
class UserUpdateView(UpdateView):
    model = User
    template_name = "user_form.html"
    form_class = UserForm
    success_url = reverse_lazy('users_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar usuario" 
        context['subtitle'] = "Editar registro de usuario"
        context['list_url'] = reverse_lazy('users_list')
        context['list'] = "Usuarios"
        return context
    
    def form_valid(self, form):
        usuario = form.instance
        password = form.cleaned_data['password']
        if 'image' in self.request.FILES:
            form.instance.image = self.request.FILES['image']
        if password:
            usuario.password = make_password(password)
        else:
            usuario.password = usuario.password
        return super().form_valid(form)


