from .acceder_lista import getListContact

def list_to_string(list):
    sentence = ""
    
    for item in list:
        if list.index(item) != 1:
            sentence += item
        else: 
            sentence += ", " + item
        
    return sentence

def set_genres(dict):
    sentence = "\n"
    
    for key in dict:
        sentence += "\t\t"+key.capitalize()+": "
        items = list_to_string(dict.get(f"{key}"))
    
        sentence += items+"\n"
    return sentence

def set_groups(groups):
    sentence = "\n"
    
    for group in groups:
        sentence += "\t\t"+group.get("nombre")+": "
        songs = list_to_string(group.get("canciones"))
        sentence += songs+"\n"
    return sentence

def consultar_contacto():
    clave = input("Escriba la clave de 3 carácteres del contacto:\n")
    contactos = getListContact()
    
    if len(clave) == 3:
        if contactos.get(f"{clave}"):
            contacto = contactos.get(f"{clave}")
            return contacto, clave
        else: 
            print("\nNo se encontró al usuario, ingreselo de nuevo")
            consultar_contacto()
    else:
        print("La clave ingresada no es de 3 carácteres ")
        consultar_contacto()
        
        
def imprimir_contacto():
    contacto = consultar_contacto()[0]
    if contacto:
        nombre = contacto.get(f"datos_personales",{}).get(f"nombre","")
        fecha = contacto.get(f"datos_personales",{}).get(f"fecha_de_nacimiento","")
        genero = contacto.get(f"datos_personales",{}).get(f"genero","")
        
        telefonos = list_to_string(contacto.get(f"datos_contacto",{}).get(f"telefonos",[]))
        email = contacto.get(f"datos_contacto",{}).get(f"email","")
        
        calle = contacto.get(f"domicilio",{}).get(f"calle_numero","")
        ciudad = contacto.get(f"domicilio",{}).get(f"ciudad","")
        entidad = contacto.get(f"domicilio",{}).get(f"entidad","")
        
        deportes = list_to_string(contacto.get(f"hobbies",{}).get(f"deportes",[]))
        películas = list_to_string(contacto.get(f"hobbies",{}).get(f"películas",[]))
        generos = set_genres(contacto.get(f"hobbies",{}).get(f"musica",{}).get("generos",{}))
        grupos = set_groups(contacto.get(f"hobbies",{}).get(f"musica",{}).get("grupos",[]))

        
        print(f"""
    ##Datos básicos
    -Nombre:\t{nombre}
    -Fecha de nacimiento:\t{fecha}
    -Género:\t{genero.upper()}, 

    ##Contacto
    -Teléfonos:\t{telefonos}
    -Email:\t{email}

    ##Domicilio
    -Calle:\t{calle}
    -Ciudad:\t{ciudad}
    -Entidad:\t{entidad}

    ##Hobbies
    -Deportes:\t{deportes}
    -Películas:\t{películas}
    -Música:
    \tGéneros:\t{generos}
    \tGrupos:\t{grupos}
    """)