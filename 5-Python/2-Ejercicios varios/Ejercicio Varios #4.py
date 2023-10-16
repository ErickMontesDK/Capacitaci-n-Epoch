num1 = int(input("Ingrese un primer número: "))
num2 = int(input("ingrese un segundo número: "))
num3 = int(input("Ingrese un tercer número: "))

def num_max_min():
    numbers = [num1, num2, num3]
    
    repeat_value = numbers.count(num1)
    
    if repeat_value == 3:
        print("Los 3 números son iguales")
    else:
        maxnumber = max(numbers)
        minnumber = min(numbers)
        print(f"El número mayor es {maxnumber} y el menor es {minnumber}")   

num_max_min()