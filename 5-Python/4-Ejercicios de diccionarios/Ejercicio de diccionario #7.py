texto = input("Escriba el texto de su telegrama: ")
longitud_max_palabra = 5
costo_palabra_corta = 5.5
costo_palabra_larga = 7

def produce_telegram(texto, long_max, costo_palabra_corta, costo_palabra_larga):
    if(texto[-1]=="."): 
        texto[-1]=" STOPSTOP"
    else:
        texto += " STOPSTOP"
        
    texto = texto.replace("."," STOP")
    palabras = texto.split(" ")
    telegrama = ""
    precio = 0
    
    for palabra in palabras:
        
        if palabra != "STOP" and palabra != "STOPSTOP":
            if len(palabra) > long_max:
                palabra = palabra[0:long_max]+"@"
                precio += costo_palabra_larga
            else:
                precio += costo_palabra_corta
            
        telegrama += " "+palabra
    print(f"Texto original: '{texto}'.\nTranscripción: '{telegrama}'.\nCosto: ${precio}.")
    
produce_telegram(texto,longitud_max_palabra,costo_palabra_corta,costo_palabra_larga)