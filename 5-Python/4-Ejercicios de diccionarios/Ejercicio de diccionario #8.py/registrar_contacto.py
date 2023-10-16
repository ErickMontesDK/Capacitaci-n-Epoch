from acceder_lista import getListContact, closeListContact
from contact_class import Contact
lista_contactos = getListContact()

contact = Contact()

def bucle_list(message, name_item):
    state = True
    list = []
    
    item = input(f"{message}")
    list.append(item)
    
    follow = input (f"Desea agregar otro {name_item} (Y) o no (N)")
    follow = follow.lower()
    
    if(follow == "n"): state = False
        
 

def bucle_dict(message, list_message, item_name, sub_item_name):
    state = True
    dicc = {}
    
    while state:
        key = input(f"{message}")
        list = bucle_list(list_message, sub_item_name)
        
        dictionario_item = { f"{key}" : list }
        dicc.update(dictionario_item)
        
        follow = input (f"Desea agregar otro {item_name} (Y) o no (N)")
        follow = follow.lower()
        
        if(follow == "n"): state = False
    return dicc
    

def get_datos_personales():
    nombre = input("Escriba el nombre de contacto: ")
    fecha_nacimiento = input("Escriba la fecha de nacimiento en formato dd-mm-aaaa: ")
    genero = input("Masculino o Femenino (Escriba 'M' o 'F')")
    
    contact.set_personal_data(nombre, fecha_nacimiento, genero)
    
def get_datos_contacto():
    teléfonos = bucle_list("Escriba el número de teléfono a agregar: ", "telefono")
    email = input("Escriba su correo electrónico: ")
    
    contact.set_contact_data(teléfonos, email)

def get_domicilio():
    calle_numero = input("Introduzca su calle y número: ")
    ciudad = input("Escriba su ciudad: ")
    entidad = input("Escriba su estado: ")
    
    contact.set_address(calle_numero, ciudad, entidad)

def get_hobbies():
    deportes = bucle_list("Escriba su deporte favorito: ", "deporte")
    peliculas = bucle_list("Escriba su película favorita: ", "película")
    music_genres = bucle_dict("Agregue uno de sus generos de música favorita: ",
        "Agregue su canción favorita de ese genero", "género","canción")
    music_artists = bucle_dict("Agregue alguno de sus grupos o artistas favoritos",
        "Escriba una canción que le guste de este artista: ","artista", "canción")
    
    contact.set_hobbies(deportes,peliculas,music_genres,music_artists)
    
# get_datos_personales()
# get_datos_contacto()
# get_domicilio()
get_hobbies()
print(contact)




        

# def get_hobbies():
#     deportes_state = True
#     musica_state = True
#     peliculas_state = True

#     deportes = []
#     música = {
#         "generos": {},
#         "grupos": {}
#     }
#     películas = []
    
        
#     while musica_state:
#         genero_state = True
        
#         música = input("Escriba su género de música favorita: ")
#         música.get("generos").update({f"{música}":[]})
        
#         canciones_state = True
        
#         while canciones_state:
#             cancion = input("Agregue una canción que le guste de ese genero: ")
#             música.get("generos").get(f"{música}").append(cancion)
        
#             seguir = input("Desea agregar otra canción (Y) o no (N): ")
#             seguir = seguir.lower()
            
#             if(seguir == "n"): canciones_state = False
        
#         seguir = input("Desea agregar otra genero de música (Y) o no (N): ")
#         seguir = seguir.lower()
        
#         if(seguir == "n"): canciones_state = False
    
    # while peliculas_state:
    #     película = int(input("Escriba su película favorita: "))
    #     películas.append(película)
        
    #     seguir = input("Desea agregar otra película (Y) o no (N): ")
    #     seguir = seguir.lower()
        
    #     if(seguir == "n"): deportes_state = False
        
    
