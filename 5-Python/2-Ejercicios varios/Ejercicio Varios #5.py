import re

letter = input("Escriba una vocal, mayúscula o minúscula: ")

def letra_mayuscula():
    matchMayus = re.search("[AEIOU]",letter)
    matchMinus = re.search("[aeiou]",letter)

    if matchMayus != None:
        return False
    elif matchMinus != None:
        return True
    else: 
        print(f"La letra {letter} no es una vocal")
        
print(letra_mayuscula())