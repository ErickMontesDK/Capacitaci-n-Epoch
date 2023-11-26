from django.forms.models import BaseModelForm
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from users.forms.users_form import UserForm
from shared.utils import getQueryFilterOption
from users.models import User
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password

class UserListView(ListView):
    model = User
    template_name = "list.html"
    
    def get_context_data(self, **kwargs):
        fields = self.model._meta.get_fields()
        
        ALL_FIELDS_MODEL = [{'name':field.name, 'type':field.get_internal_type(), 'choices':field.choices if hasattr(field, 'choices') else None} for field in fields] 
        fieldsToShow = ['id','username','first_name','last_name','email','rol','genero']
        fieldsInModel = [element for element in ALL_FIELDS_MODEL if element['name'] in fieldsToShow]
        context = super().get_context_data(**kwargs)
        context['fields'] = fieldsInModel
        context["title"] = "Usuarios" 
        context['subtitle'] = "Lista de usuarios registradas"
        context['total_records'] = User.objects.count()
        context['add_element'] = reverse_lazy('user_add')
        context['model'] = 'usuario'
        context['list_url'] = reverse_lazy('users_list')
        return context
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        page = int(self.request.GET.get('page', 1))
        orderBy = self.request.GET.get('orderBy', 'id')
        query = super().get_queryset().order_by(orderBy)
        campos = self.request.GET
                
        filters = getQueryFilterOption(campos)
        
        if filters != {}:
            query = query.filter(**filters)

        page_size = 10
        
        pagination = Paginator(query, page_size, 0, True)
        page = pagination.page(page)
        return page, query.count()
    
    def get(self, request, *args, **kwargs):
        self.object_list, query_size = self.get_queryset() # Aquí llamas al método get_queryset
        context = self.get_context_data(**kwargs) 
        
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            template_name = "user_table.html"
            html = render_to_string(template_name, context)
            return JsonResponse({"html": html, "query_size":query_size})
        return super().get(request, *args, **kwargs)
    
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


