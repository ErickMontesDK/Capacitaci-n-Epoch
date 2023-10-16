string = input("Escriba una cadena de texto: ")
number = int(input("Escriba un número entero: "))
index = 0

while index <= len(string)-number:    
    print(f"{string[index:index+number]}")
    
    index += 1
