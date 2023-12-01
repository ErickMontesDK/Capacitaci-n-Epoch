from .acceder_lista import getListContact, writeListContact
from .contact_class import Contact
from .consultar_contacto import consultar_contacto

seccion = 1

class ContactManager:
    lista_contactos = getListContact()
    SECTIONS = {
        'datos personales' : 1,
        'contacto' : 2,
        'domicilio' : 3,
        'hobbies' : 4,
        'guardar' : 5,
        'cancelar' : 6
    }
    contact = {}
    id = ''
    
    @staticmethod
    def createNewContact():
        ContactManager.contact = Contact()
        ContactManager.register_contact_cycle()
        ContactManager.id = list(ContactManager.contact.get_contact().keys())[0]
        
    @staticmethod
    def modifiedOldContact():
        contact = consultar_contacto()
        
        ContactManager.contact = Contact()
        full_contact = {contact[1]: contact[0]} 
        
        ContactManager.contact.modifiedContact(full_contact, contact[1])
        ContactManager.register_contact_cycle()
        ContactManager.id = list(ContactManager.contact.get_contact().keys())[0]
        
    @staticmethod
    def input_to_list(input_str):
        user_input = input_str.lower().split(",")
        return [item.strip() for item in user_input]
    
    @staticmethod
    def input_to_dict(main_item_msg, sub_item_name):
        dictionary = {}
        user_input = input(f"{main_item_msg}")
        if user_input != "":
            user_input = user_input.lower().split(",")
            user_input = [item.strip() for item in user_input]
            
            for element in user_input:
                sub_item_list = input(f"Agregue l@s {sub_item_name} del elemento {element}, separados por una coma:\n")
                sub_item_list = ContactManager.input_to_list(sub_item_list)
                dictionary[element] = sub_item_list
            return dictionary
        else:
            return {}

    @staticmethod
    def ask_input(msg, old_value):
        old_label = False
        if old_value != "" and old_value != {} and old_value != []:
            print(f"Anteriormente ingresado: {old_value}")
            old_label = True

        dato = input(msg)
        if dato == "":
            if old_label: print(f'Conservando anterior ingreso: {old_value}\n')
            return old_value
        else:
            print(f"Ingresado : {dato}\n")
            return dato
    
    @staticmethod
    def set_personal_info():
        porcentaje = ContactManager.contact.porcentage_status()
        nombre = fecha_nacimiento = genero = ""
        
        if("datos_personales") in ContactManager.contact.get_inside_contact():
            route = ContactManager.contact.get_inside_contact().get("datos_personales")
            porcentaje -= 20
            nombre = route.get("nombre")
            fecha_nacimiento = route.get("fecha_de_nacimiento")
            genero = route.get("genero")
        
        print("\n##DATOS PERSONALES\n")
        nombre = ContactManager.ask_input(f"{porcentaje}% Escriba el nombre de contacto: \n", nombre)
        porcentaje += 10
        fecha_nacimiento = ContactManager.ask_input(f"{porcentaje}% Escriba la fecha de nacimiento en formato dd-mm-aaaa: \n", fecha_nacimiento)
        porcentaje += 5
        
        def generoFunction(old_genero):
            genero = ContactManager.ask_input(f"{porcentaje}% Masculino o Femenino (Escriba 'M' o 'F'): \n", old_genero)
            genero = genero.lower()
            print(genero)
            if genero != "m"and genero != "f" and genero != "":
                print(f"'{genero}' no es un valor válido.")
                generoFunction(old_genero)
            return genero
        genero = generoFunction(genero)
        
        return ContactManager.contact.set_personal_data(nombre, fecha_nacimiento, genero)
    
    @staticmethod
    def set_contact_info():
        porcentaje = ContactManager.contact.porcentage_status()
        teléfonos = email = ""
        
        if("datos_contacto") in ContactManager.contact.get_inside_contact():
            porcentaje -= 20
            route = ContactManager.contact.get_inside_contact().get("datos_contacto")
            teléfonos = ", ".join(str(telephone) for telephone in route.get("telefonos"))
            email = route.get("email")
        print("\n##DATOS DE CONTACTO\n")
        teléfonos = ContactManager.input_to_list(ContactManager.ask_input(f"{porcentaje}% Escriba los números telefonicos a agregar, separados por una coma: \n", teléfonos))           
        porcentaje += 10
        email = ContactManager.ask_input(f"{porcentaje}% Escriba su correo electrónico: \n", email)
        
        return ContactManager.contact.set_contact_data(teléfonos, email)
    
    @staticmethod
    def set_domicilio():
        porcentaje = ContactManager.contact.porcentage_status()
        calle_numero = ciudad = entidad = ""
        
        if("domicilio") in ContactManager.contact.get_inside_contact():
            porcentaje -= 15
            route = ContactManager.contact.get_inside_contact().get("domicilio")
            calle_numero = route.get("calle_numero")
            ciudad = route.get("ciudad")
            entidad = route.get("entidad")    
                    
        print("\n##DOMICILIO\n")
        calle_numero = ContactManager.ask_input(f"{porcentaje}% Introduzca su calle y número: \n", calle_numero)
        porcentaje += 5
        ciudad = ContactManager.ask_input(f"{porcentaje}% Escriba su ciudad: \n", ciudad)
        porcentaje += 5
        entidad = ContactManager.ask_input(f"{porcentaje}% Escriba su estado: \n", entidad)  
        
        return ContactManager.contact.set_address(calle_numero, ciudad, entidad) 
    
    @staticmethod
    def set_hobbies():
        porcentaje = ContactManager.contact.porcentage_status()
        deportes = peliculas = ""
        music_genres = music_artists = {}
        
        if("hobbies") in ContactManager.contact.get_inside_contact():
            porcentaje -= 40
            route = ContactManager.contact.get_inside_contact().get("hobbies")
            deportes = ", ".join(str(x) for x in route.get("deportes"))
            peliculas = ", ".join(str(x) for x in route.get("películas"))
            music_genres = route.get("musica").get("generos")
            music_artists = {group["nombre"]: group["canciones"] for group in route.get("musica").get("grupos")}
        
        print("\n##PASATIEMPOS Y GUSTOS\n")
        deportes = ContactManager.input_to_list(ContactManager.ask_input(f"{porcentaje}% Escriba sus deportes favoritos, separados por una coma: \n", deportes))
        peliculas = ContactManager.input_to_list(ContactManager.ask_input(f"{porcentaje}% Escriba sus películas favoritas, separados por una coma: \n", peliculas))
        music_genres_new = ContactManager.input_to_dict(f"{porcentaje}% Agregue sus géneros favoritos de música: \n", "canciones favoritas")
        if music_genres_new != {}: music_genres = music_genres_new 
        music_artists_new = ContactManager.input_to_dict(f"{porcentaje}% Agregue alguno de sus grupos o artistas favoritos: \n","canciones favoritas")
        if music_artists_new != {}: music_artists = music_artists_new 
        
        
        return ContactManager.contact.set_hobbies(deportes,peliculas,music_genres,music_artists)
        
    @staticmethod
    def save_contact():      
        new_contact = ContactManager.contact.get_contact()
        ContactManager.lista_contactos.update(new_contact)
        writeListContact(ContactManager.lista_contactos)
        
    @staticmethod
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
            seccion = ContactManager.SECTIONS.get(f"{after_section}")
            ContactManager.contact.save_entry(entry)
            ContactManager.save_contact()
            
        elif follow_section == "b" and not before_section == "cancelar":
            seccion = ContactManager.SECTIONS.get(f"{before_section}")
        elif follow_section == "c":
            seccion = ContactManager.SECTIONS["cancelar"]
        else: 
            print("Escoja una opción válida")
            ContactManager.change_section(entry, section, after_section, before_section)
            
    
    @staticmethod
    def register_contact_cycle():
        global seccion
        seccion = 1
        
        while seccion != ContactManager.SECTIONS["cancelar"]:
            if seccion == 1:
                entry = ContactManager.set_personal_info()
                ContactManager.change_section(entry, "datos personales", "contacto")
            elif seccion == 2:
                entry = ContactManager.set_contact_info()
                ContactManager.change_section(entry, "contacto", "domicilio", "datos personales")
                
            elif seccion == 3:
                entry = ContactManager.set_domicilio()
                ContactManager.change_section(entry, "domicilio", "hobbies", "contacto")
                
            elif seccion == 4:
                entry = ContactManager.set_hobbies()
                ContactManager.change_section(entry, "hobbies", "guardar", "domicilio")
            elif seccion == 5:
                ContactManager.save_contact()
                print("\nContacto guardado\n")
                seccion = ContactManager.SECTIONS["cancelar"]
        

