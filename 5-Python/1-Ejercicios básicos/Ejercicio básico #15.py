barras = int(input("Barras vendidas que no son del día: "))
precio = 3.49
descuento = precio*.6

total = (precio - descuento)*barras

print("Precio individual: ${}.\nDescuento por pieza: ${}.\nCosto final: ${}".format(round(precio, 2), round(descuento, 2), round(total, 2)))

