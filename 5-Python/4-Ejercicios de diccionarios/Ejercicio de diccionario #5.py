date = input("Escriba una fecha en formato dd/mm/aaaa: ")

meses = {
    "01":"Enero", "02":"Febrero", "03":"Marzo", "04":"Abril", "05":"Mayo", "06":"Junio", 
    "07":"Julio", "08":"Agosto", "09":"Septiembre", "10":"Octubre", "11":"Noviembre", "12":"Diciembre"
}

date_values = date.split("/")

def validate_month(month):
    if int(month) < 10:
        month = f"0{int(month)}"
        
    return meses.get(month,"algún mes")

sentence = f"{date_values[0]} de {validate_month(date_values[1])} del {date_values[2]}"
print(sentence)