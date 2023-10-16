divisas = { 'EUR':'21.50', 'USD':'18.80', 'YEN':'12.56'}

divisa_user = input("Escriba que tipo de divisa ('EUR', 'USD', 'YEN'): ")

def divisaSelected(divisa):
    divisa = divisa.upper()
    
    if divisa in divisas: 
        convertImport(divisa, divisas[divisa])
    else: 
        print(f"No se encontró la divisa {divisa}, vuelva a intentarlo")
    
def convertImport(divisa, valor):
    importe = float(input("¿Cuanto importe desea convertir a pesos mexicanos?: "))
    result = float(valor)*importe
    print(f"{round(importe, 2)}{divisa} es igual a ${round(result, 2)} pesos mexicanos")
    
divisaSelected(divisa_user)