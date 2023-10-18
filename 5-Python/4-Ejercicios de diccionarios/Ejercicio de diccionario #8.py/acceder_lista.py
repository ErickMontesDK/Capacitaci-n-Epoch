import json
urlFile = "D:/erick/Documents/Codes/Epoch Capacitación/5-Python/4-Ejercicios de diccionarios/Ejercicio de diccionario #8.py/agenda_db.txt"

def getListContact():
    file = open(urlFile,"r")
    data = json.load(file)
    file.close()
    return data
    
def writeListContact(listContact):
    file = open(urlFile,"w")
    json.dump(listContact, file, indent=6)
    file.close()