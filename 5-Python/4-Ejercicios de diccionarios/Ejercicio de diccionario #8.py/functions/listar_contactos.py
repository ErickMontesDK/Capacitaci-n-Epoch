from .acceder_lista import getListContact

def getContactList():
    contacts = getListContact()
    
    for contact in contacts:
        print(f"""
-Clave: \t{contact}
    -Nombre:\t{contacts[f"{contact}"].get("datos_personales").get("nombre")}
    -Fecha de registro:\t{contacts[f"{contact}"].get("fecha_registro")}
    -Porcentaje de llenado:\t{contacts[f"{contact}"].get("porcentaje")}
""")
    
        


