print("Juego del Ahorcado")
palabra = input("Ingresa la faltante para el juego: ")
intentos = 0

faltante = list(palabra)
resultado = list("*"*len(faltante))

while intentos < 5:
    letra = input("Dime con que letra quieres jugar: ")
    intentos += 1
    
    if letra in faltante:
        index = faltante.index(letra)
        faltante[index]="*"
        resultado[index]=letra
        print(f"¡Acierto! La letra {letra} si aparece. de momento llevas formado:\n{resultado}")
    else:
        print(f"¡Falló! Te quedán {5-intentos} intentos")
        
    if not "*" in resultado:
        print(f"Felicidades, adiviniste la faltante escondida {''.join(resultado)}")
        break
if "*" in resultado:
        print(f"Se acabaron lod intentos. , la palabra escondida era {palabra}")