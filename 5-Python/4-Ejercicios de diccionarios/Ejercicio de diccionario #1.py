user_number = int(input("Ingrese un número entero del 1 al 999: "))


def nombrar_numero(numero):
    digitos = {
        1: "uno",   2: "dos",   3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez", 
        11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince", 16: "dieciseis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve",
        20: "veinte", 30: "treinta", 40: "cuarenta", 50: "cincuenta", 60: "sesenta", 70: "setenta",80: "ochenta", 90: "noventa",
        100: "cien", 200: "doscientos", 300:"trescientos", 400:"cuatrocientos", 500:"quinientos", 600:"seiscientos", 700:"setecientos",
        800:"ochocientos", 900: "novecientos"
    }
    sentence = ""

    if numero >=100: 
        centenas = (numero//100)*100
        sentence += digitos[centenas]
        
        if(numero>100 and numero<200): 
            sentence+="to"
            
        numero -= centenas
        
        if(numero)>0: sentence+=" "
                
    if numero >= 10: 
        if numero >= 10 and numero < 20:
            sentence += digitos[numero]
            numero = 0
            
        else:
            decenas = ((numero)//10)*10
            sentence += digitos[decenas]
            
            numero -= decenas
            
            if numero > 0: sentence+=" y "
            
    if numero >  0: 
        sentence +=digitos[numero]

    return sentence


if user_number < 1000:
    print(nombrar_numero(user_number))
    
else:
    print(f"El número {user_number} no está dentro del rango 1 al 999")