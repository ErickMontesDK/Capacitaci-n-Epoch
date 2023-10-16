dividendo = int(input("Escriba un primer número entero: "))
divisor = int(input("Escriba un segundo número entero: "))

cociente = dividendo // divisor
resto = dividendo % divisor 

print("{} entre {} da un cociente {} y un resto {}".format(dividendo, divisor, cociente, resto))