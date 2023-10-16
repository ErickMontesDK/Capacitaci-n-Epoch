from diccionario import morse_code

def translate_morse (texto):
    texto = texto.lower().replace("\n"," ").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n")
    traduccion = ""
    
    for i in range(len(texto)):
        if texto[i] in morse_code:
            traduccion += morse_code[texto[i]]+";"

    print(f"Texto original: '{texto}'.\nCódigo morse: {traduccion}") 


if __name__=="__main__":
    user_text = input("Escriba el texto a traducir a morse: ")
    translate_morse(user_text)

