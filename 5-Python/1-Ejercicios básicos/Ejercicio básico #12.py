cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Interés anual en porcentaje %: "))
años = int(input("Número de años: "))

capital = cantidad * (1 + (interes*0.01)) ** años

print("El capital acumulado es: $", round(capital, 2))




