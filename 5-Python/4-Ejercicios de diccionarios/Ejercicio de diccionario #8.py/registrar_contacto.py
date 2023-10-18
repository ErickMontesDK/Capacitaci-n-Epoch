from acceder_lista import getListContact, writeListContact
from contact_class import Contact

lista_contactos = getListContact()
porcentaje_avance = 0

secciones = {
    'datos personales' : 1,
    'contacto' : 2,
    'domicilio' : 3,
    'hobbies' : 4,
    'guardar' : 5,
    'cancelar' : 6
}

contact = {}

def bucle_list(message):
    list = input(f"{message}").lower().split(",")
    return [item.strip() for item in list]
    

def bucle_dict(main_item_message, sub_item_name):
    diccionary = {}
    
    dicc_elements = input(f"{main_item_message}").lower().split(",")
    dicc_elements = [item.strip() for item in dicc_elements]
    
    for element in dicc_elements:
        list = bucle_list(f"Agregue l@s {sub_item_name} del elemento {element}, separados por una coma: \n")
        
        diccionary.update({f'{element}': list})

    return diccionary

def get_datos_personales():
    porcentaje_avance = contact.porcentage_status()
    
    if "datos_personales" in contact.get_keys():
        porcentaje_avance -= 20
        
    nombre = input(f"{porcentaje_avance}% Escriba el nombre de contacto: \n")
    porcentaje_avance += 10
    fecha_nacimiento = input(f"{porcentaje_avance}% Escriba la fecha de nacimiento en formato dd-mm-aaaa: \n")
    porcentaje_avance += 5
    genero = input(f"{porcentaje_avance}% Masculino o Femenino (Escriba 'M' o 'F'): \n")
    
    return contact.set_personal_data(nombre, fecha_nacimiento, genero)
    
def get_datos_contacto():
    porcentaje_avance = contact.porcentage_status()
    
    if "datos_contacto" in contact.get_keys():
        porcentaje_avance -= 20
        
    porcentaje_avance += 10
    teléfonos = bucle_list(f"{porcentaje_avance}% Escriba los números telefonicos a agregar, separados por una coma: \n")
    porcentaje_avance += 10
    email = input(f"{porcentaje_avance}% Escriba su correo electrónico: \n")
    
    return contact.set_contact_data(teléfonos, email)

def get_domicilio():
    porcentaje_avance = contact.porcentage_status()
    
    if "domicilio" in contact.get_keys():
        porcentaje_avance -= 15
        
    calle_numero = input(f"{porcentaje_avance}% Introduzca su calle y número: \n")
    porcentaje_avance += 5
    ciudad = input(f"{porcentaje_avance}% Escriba su ciudad: \n")
    porcentaje_avance += 5
    entidad = input(f"{porcentaje_avance}% Escriba su estado: \n")
    
    return contact.set_address(calle_numero, ciudad, entidad)

def get_hobbies():
    porcentaje_avance = contact.porcentage_status()
    
    if "hobbies" in contact.get_keys():
        porcentaje_avance -= 40
        
    deportes = bucle_list(f"{porcentaje_avance}% Escriba sus deportes favoritos, separados por una coma: \n")
    porcentaje_avance += 10
    peliculas = bucle_list(f"{porcentaje_avance}% Escriba sus películas favoritas, separados por una coma: \n")
    porcentaje_avance += 10
    music_genres = bucle_dict(f"{porcentaje_avance}% Agregue sus géneros favoritos de música: \n",
        "canciones favoritas")
    porcentaje_avance += 10
    music_artists = bucle_dict(f"{porcentaje_avance}% Agregue alguno de sus grupos o artistas favoritos: \n",
        "canciones favoritas")
    
    print(music_artists, music_genres)
    
    return contact.set_hobbies(deportes,peliculas,music_genres,music_artists)

def save_contact():
    new_contact = contact.get_contact()
    lista_contactos.update(new_contact)
    writeListContact(lista_contactos)
    
seccion = 0

def change_section (entry, section, after_section, before_section="cancelar"):    
    global seccion
    
    if before_section=="cancelar":
        follow_section = input(f"""\nSeleccione una opción
Guardar (A) la información en {section.upper()} y continuar con {after_section.upper()}\n
Cancelar (C) para regresar al menú principal: """)
    else: 
        follow_section = input((f"""\nSeleccione una opción
Guardar (A) la información en {section.upper()} y continuar con {after_section.upper()}\n
Regresar (B) regresar a la sección anterior de {before_section.upper()} sin guardar lo escrito\n
Cancelar (C) para regresar al menú principal: """))
    
    follow_section =  follow_section.lower()
    
    if follow_section == "a":
        seccion = secciones.get(f"{after_section}")
        contact.save_entry(entry)
        save_contact()
    elif follow_section == "b" and not before_section == "cancelar":
        seccion = secciones.get(f"{before_section}")
    elif follow_section == "c":
        seccion = secciones["cancelar"]
    else: 
        print("Escoja una opción válida")
        change_section(entry, section, after_section, before_section)
        
        
def registrar_contacto_cicle():
    global seccion
    
    while seccion != secciones["cancelar"]:
        if seccion == 0:
            global contact
            contact = Contact()
            print(contact)
            seccion = secciones["datos personales"]
            
        if seccion == 1:
            entry = get_datos_personales()    
            change_section(entry, "datos personales", "contacto")
            
        elif seccion == 2:
            entry = get_datos_contacto()
            change_section(entry, "contacto", "domicilio", "datos personales")
            
        elif seccion == 3:
            entry = get_domicilio()
            change_section(entry, "domicilio", "hobbies", "contacto")
            
        elif seccion == 4:
            entry = get_hobbies()
            change_section(entry, "hobbies", "guardar", "domicilio")
            
        elif seccion == 5:
            save_contact()
            print("\nContacto guardado\n")
            seccion = secciones["cancelar"]

