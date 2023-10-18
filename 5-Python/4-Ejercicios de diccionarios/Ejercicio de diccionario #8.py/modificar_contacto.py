from consultar_contacto import consultar_contacto
from registrar_contacto import get_datos_personales

def change_datos_personales(contacto):
    porcentaje_avance = contacto.get("porcentaje")
    
    if contacto.get("datos_personales"):
        porcentaje_avance -= 20
        
    nombre = input(f"{porcentaje_avance}% Escriba el nombre de contacto: \n")
    if nombre == "" and contacto.get("datos_personales").get("nombre"): 
        nombre = contacto.get("datos_personales").get("nombre")
    porcentaje_avance += 10
    print(nombre)
    
    fecha_nacimiento = input(f"{porcentaje_avance}% Escriba la fecha de nacimiento en formato dd-mm-aaaa: \n")
    if fecha_nacimiento == "" and contacto.get("datos_personales").get("fecha_de_nacimiento"): 
        fecha_nacimiento = contacto.get("datos_personales").get("fecha_de_nacimiento")
    porcentaje_avance += 5
    print(fecha_nacimiento)
    
    genero = input(f"{porcentaje_avance}% Masculino o Femenino (Escriba 'M' o 'F'): \n")
    if genero == "" and contacto.get("datos_personales").get("genero"): 
        genero = contacto.get("datos_personales").get("genero")
    print(genero)
    return contacto.set_personal_data(nombre, fecha_nacimiento, genero)

def modificar_contacto():
    contacto = consultar_contacto()
    
    
modificar_contacto()

def bucle_list(message):
    state = True
    list = input(f"{message}")
    list = list.lower().split(",")
    list = [item.strip() for item in list]
    return list

def bucle_dict(main_item_message, sub_item_name):
    diccionary = {}
    
    dicc_elements = input(f"{main_item_message}")
    dicc_elements = dicc_elements.lower().split(",")
    dicc_elements = [item.strip() for item in dicc_elements]
    
    for element in dicc_elements:
        list = bucle_list(f"Agregue l@s {sub_item_name} del elemento {element}, separados por una coma: \n")
        
        diccionary.update({f'{element}': list})

    return diccionary

def ask_input(msg, old_value):
    dato = input(msg)
    if dato == "":
        return old_value
    else:
        return dato

def get_datos_personales(contacto):
    porcentaje = contacto.get["porcentaje"]
    nombre, fecha_nacimiento, genero = ""
    
    if contacto.get("datos_personales"):
        porcentaje_avance -= 20
        nombre = contacto.get("datos_personales").get("nombre")
        fecha_nacimiento = contacto.get("datos_personales").get("fecha_de_nacimiento")
        genero = contacto.get("datos_personales").get("genero")

    nombre = ask_input(f"{porcentaje}% Escriba el nombre de contacto: \n", nombre)
    porcentaje += 10
    fecha_nacimiento = ask_input(f"{porcentaje}% Escriba la fecha de nacimiento en formato dd-mm-aaaa: \n", fecha_nacimiento)
    porcentaje += 5
    genero = ask_input(f"{porcentaje}% Masculino o Femenino (Escriba 'M' o 'F'): \n", genero)
    
def get_datos_contacto(contacto):
    porcentaje = contacto.get["porcentaje"]
    teléfonos, email = ""
    
    if contacto.get("datos_contacto"):
        porcentaje -= 20
        teléfonos = ", ".join(str(x) for x in contacto.get("datos_contacto").get("telefonos"))
        email = contacto.get("datos_contacto").get("email")
        
    teléfonos = bucle_list(ask_input(f"{porcentaje}% Escriba los números telefonicos a agregar, separados por una coma: \n", teléfonos))
    email = ask_input(f"{porcentaje}% Escriba su correo electrónico: \n", email)  