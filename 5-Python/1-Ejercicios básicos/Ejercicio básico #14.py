deposito = float(input("Cantidad depositada: "))

ahorro_año_1 = round((deposito * (1 + 0.04 )**1), 2)
ahorro_año_2 = round((deposito * (1 + 0.04 )**2), 2)
ahorro_año_3 = round((deposito * (1 + 0.04 )**3), 2)

print("Ahorros primer año: ${}.\nAhorros segundo año: ${}.\nAhorros tercer año: ${}.".format(ahorro_año_1, ahorro_año_2, ahorro_año_3))