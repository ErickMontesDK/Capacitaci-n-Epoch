precio = input("Escriba el precio del producto: ")
iva = float(precio)*0.16
total = float(precio)+iva

print("Importe introducido: ${}.\nIVA: ${}.\nPrecio final: ${}.".format(precio,iva,total))