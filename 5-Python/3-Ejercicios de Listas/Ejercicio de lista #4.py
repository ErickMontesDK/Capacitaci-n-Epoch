lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def elimina(lista):
    if len(lista) > 2:
        lista_reducida = lista[1:-1]
        return lista_reducida
    else:
        return []
    
def media(lista):
    lista_reducida = elimina(lista)
    lista_segundo_recorte = elimina(lista_reducida)
    return lista_segundo_recorte

print(f"Lista original: {lista}")
print(f"Lista función elimina(): {elimina(lista)}")
print(f"Lista función media(): {media(lista)}")


