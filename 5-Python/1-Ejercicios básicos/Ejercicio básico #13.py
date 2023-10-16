payasos = int(input("Ingrese cantidad de payasos: "))
muñecas = int(input("Ingrese cantidad de muñecas: "))

peso = (payasos * 112) + (muñecas * 75)

print("El paquete pesará un total de: "+str(peso/1000)+" kg")