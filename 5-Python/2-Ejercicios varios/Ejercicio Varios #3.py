num1 = int(input("Ingrese un primer número: "))
num2 = int(input("ingrese un segundo número: "))

def menorque():
    if num1 < num2: 
        print(f"El primer número {num1} es menor a {num2}")
    elif num2 < num1: 
        print(f"El segundo número {num2} es menor a {num1}")
    else: 
        print("Ambos números son iguales")
        
menorque()