from django.forms import EmailInput, FileInput, ModelForm, PasswordInput, TextInput
from users.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email","image","rol","genero","password")
        labels = {
            'username':'Nombre de usuario',
            'first_name':"Nombre",
            'last_name':"Apellidos",
            'email':"Correo electrónico",
            "image":"Imagen de perfil",
            "rol":"Rol del usuario",
            "genero":"Género",
            "password":"Contraseña"
        }
        widgets = {
            'username':TextInput(
                attrs = {
                    'placeholder':'Escriba su usuario',
                }
            ),
            'first_name': TextInput(
                attrs = {
                    'placeholder':'Escriba su nombre'
                }
            ),
            'last_name': TextInput(
                attrs = {
                    'placeholder':'Escriba sus apellidos'
                }
            ),
            'email': EmailInput(
                attrs = {
                    'placeholder':'Escriba su correo electrónico'
                }
            ),
            'password':PasswordInput(
                attrs = {
                    'placeholder':"Cree una contraseña"
                }
            ),
            'image':FileInput(
                attrs={'accept': 'image/*'}
            )
        }
