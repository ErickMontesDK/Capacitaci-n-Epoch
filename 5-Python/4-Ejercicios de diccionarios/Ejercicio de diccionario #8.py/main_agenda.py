from registrar_contacto import registrar_contacto_cicle
from listar_contactos import getContactList
from consultar_contacto import imprimir_contacto
from registro_modificacion_contacto import ContactManager
# from modificar_contacto import modificar_contacto

print("\nBIENVENIDO A LA AGENDA DE CONTACTOS\n")

menu_option = {
    "Listar": 1,
    "Registrar": 2,
    "Consultar": 3,
    "Modificar": 4,
    "Salir": 5
}

def select_section():
    section =""
    
    while section != menu_option["Salir"]:
        section = input("""Escoja alguna de las sig. opciones:\n
    1.Listar contactos
    2.Registrar contactos
    3.Consultar contacto
    4.Modificar contacto
    5.Salir
    """)      
        try:
            section = int(section)
            
            if int(section) == menu_option["Listar"]:
                getContactList()
                
            elif int(section) == menu_option["Registrar"]:
                ContactManager.createNewContact()

            elif int(section) == menu_option["Consultar"]:
                imprimir_contacto()
                
            elif int(section) == menu_option["Modificar"]:
                ContactManager.modifiedOldContact()
            
            elif int(section) == menu_option["Salir"]:
                print("\nAdios. Hasta pronto\n")         
            else:
                print(f"\nNo existe la opción '{section}'. Vuelva a intentarlo\n")
            
        except ValueError:
            print(f"El valor introducido '{section}' no es válido. Vuelve a intentarlo")

                    



if __name__=="__main__":      
    select_section()