texto = """Mientras observábamos la extraña visión que teníamos 
ante los ojos, los gruesos labios se abrieron y brotaron 
algunos sonidos, tras lo cual el ser se relajó y murió."""

texto = texto.replace("\n","")

palabras = texto.split(" ")
cadena_iniciales = ""

for palabra in palabras:
    letra = palabra[0].capitalize()
    cadena_iniciales += letra
    
print(cadena_iniciales)
