from django.contrib.auth.decorators import user_passes_test

def es_administrador(user):
    return user.is_authenticated and user.rol == "administrador"

def es_vendedor(user):
    return user.is_authenticated and user.rol == "vendedor"

administrador_required = user_passes_test(es_administrador, login_url='/dashboard/')
vendedor_required = user_passes_test(es_vendedor, login_url='/dashboard/')