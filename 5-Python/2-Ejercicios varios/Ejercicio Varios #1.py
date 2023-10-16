print("Programa de calificaciones.\nNecesito que me des las calificaciones de tus dos exámenes")

exam1 = float(input("Calificación primer parcial: "))
exam2 = float(input("Calificación segundo parcial: "))

promedio = (exam1 + exam2)/2

print(f"Tu nota final es de {promedio}")

if exam1 < 5 and exam2 < 5: 
    print("No aprobaste. Te fue mal en ambos examenes.")

elif exam1 < 5: 
    print("No aprobaste. Tienes que repetir el primer parcial.")
    
elif exam2 < 5: 
    print("No aprobaste: Tienes que repetir el segundo parcial.")

else:
    print("Aprobaste el curso.")