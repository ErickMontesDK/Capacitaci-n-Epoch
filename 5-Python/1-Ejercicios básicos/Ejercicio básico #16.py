number = input("Ingrese un número: ")

try:
    number = float(number)
except ValueError:
    print("La variable no es un digito")

if number >= 0 and number <= 10:
    print("El número está entre 0 y 10")
elif number >= 11 and number <= 20:
    print("El número está entre 11 y 20")
elif number >= 21 and number <= 30:
    print("El número está entre 21 y 30")
elif number < 0:
    print("El número es menor a 0")
else:
    print("El número es mayor a 30")
    

