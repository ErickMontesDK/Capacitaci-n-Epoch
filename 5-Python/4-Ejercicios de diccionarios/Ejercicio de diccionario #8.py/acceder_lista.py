import json

file = open("D:/erick/Documents/Codes/Epoch Capacitación/5-Python/4-Ejercicios de diccionarios/Ejercicio de diccionario #8.py/agenda_db.txt","r")

def getListContact():
    data = json.load(file)
    return data

def closeListContact():
    file.close()