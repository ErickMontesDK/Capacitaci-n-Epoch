peso = float(input("Ingrese su peso: "))
estatura = float(input("Ingrese su estatura en metros: "))
imc = round(peso/(estatura**2), 2)

print("Tu índice de masa corporal es: "+str(imc))