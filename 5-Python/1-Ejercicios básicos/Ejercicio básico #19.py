import random 
number = random.randrange(1, 50)
intento = 0

print("¿Del 1 al 50, en que número estoy pensando?")

while intento < 3:
    user_number = int(input("Escribe tu número: "))
    
    if user_number == number:
        print(f"¡Felicidades! Adiviniste que estaba pensando en el número {number}")
        break
    elif user_number < number:
        print("¡Fallaste! El número que pienso es más grande")
    else:
        print("¡Fallaste! El número que pienso es más chico")
    
    intento += 1
    
    if intento == 3 : 
        print(f"Estaba pensando en el {number}. Suerte a la próxima")
    else: 
        print(f"Tienes todavia {3-intento} intentos")
