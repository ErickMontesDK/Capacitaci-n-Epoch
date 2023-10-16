username = input("Escriba su nombre de usuario: ")

userlength = len(username)

def alfanumerico ():
    for char in username:
        if not char.isalnum():
            return False
    return True
    
    
def validacion_username ():
    if userlength > 6 and userlength <= 12 and alfanumerico():
        return True
    elif userlength < 6:
        print("El nombre de usuario debe contener al menos 6 caracteres")
    elif userlength > 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")
    else:
        print("El nombre de usuario puede contener solo letras y números")
        
print(validacion_username())
        
        

        