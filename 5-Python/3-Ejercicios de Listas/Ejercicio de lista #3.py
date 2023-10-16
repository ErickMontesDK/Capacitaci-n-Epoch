año_inicial = int(input("Año inicial: "))
año_final = int(input("Año final: "))

años = []
ingresos = []
gastos = []
beneficios = []
años_con_beneficios = []
años_con_perdidas = []

for año in range(año_inicial, año_final + 1):
    años.append(año)
    
    ingreso = int(input(f"Ingresos del año {año}: "))
    gasto = int(input(f"Gastos del año {año}: "))
    
    beneficio = ingreso - gasto
    hay_beneficio = beneficio > 0
    
    ingresos.append(ingreso)
    gastos.append(gasto)
    beneficios.append(beneficio)
    
    print(f"Año:{año}. Beneficio: ${beneficio}. Hubo beneficio: {hay_beneficio}.")
    
    if hay_beneficio:
        años_con_beneficios.append(año)
    else:
        años_con_perdidas.append(año)

print(f"Años con beneficios: {años_con_beneficios}")
print(f"Años con pérdidas: {años_con_perdidas}")
