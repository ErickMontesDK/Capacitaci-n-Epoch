import re

nombre = input("Escriba su nombre: ")
cuenta = 0

for letra in nombre:
    if re.search("[aeiouAEIOUáéíóúöü]",letra) != None: cuenta+=1
    
print(f"Su nombre tiene {cuenta} vocales")