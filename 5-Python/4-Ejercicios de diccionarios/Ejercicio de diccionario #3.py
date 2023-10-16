usuarios = {
    1 : { 'usuario': 'avilla', 'contrasena':'alex2020', 'nombre': 'Alejandro Villa Gonzalez' },  
    2 : { 'usuario': 'jperez', 'contrasena':'juan83*', 'nombre': 'Juan Perez Lopez' },  
    3 : { 'usuario': 'agarcia', 'contrasena':'moReliA150#', 'nombre' : 'Andrea Garcia Gil' },
}

def validate_password(user_info):
    intento_password = 0
    password_valid = False
    
    while intento_password < 3 and not password_valid:
        password_input = input("Escriba su contraseña: ")
        
        if password_input == user_info.get("contrasena"): 
            print(f"Bienvenido {user_info.get('usuario')}")
            password_valid = True
            break
        else:    
            print("Contraseña incorrecta, por favor reintentelo")
            intento_password += 1
    if not password_valid: print("Demasiados intentos fallidos. Intentelo más tarde")
        
        
        
def validate_user():
    intento_user = 0
    user_found = False
    
    while intento_user < 3 and not user_found:
        intento_user += 1
        user_input = input("Ingrese su nombre de usuario: ")
        
        for i in usuarios:
            if user_input==usuarios[i].get("usuario"): 
                validate_password(usuarios[i])
                user_found = True
                break
        
        if not user_found: print("No se encontró al usuario, vuelva a intentarlo")
        
    if not user_found: print("Demasiados intentos de usuario. Intentelo más tarde")
    
validate_user()
    

        
        