from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView, login_required
from django.views.generic import TemplateView

def root(request):
    return redirect('dashboard')

class dashboard(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Dashboard' 
        return context

class LoginFormView(LoginView):
    template_name = "login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Iniciar sesión" 
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)