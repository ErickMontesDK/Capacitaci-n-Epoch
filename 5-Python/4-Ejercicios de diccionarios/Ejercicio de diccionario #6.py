buy_car = {}
state = True

def add_product():
    producto = input("Escriba el producto: ")
    precio = input(f"Escriba el precio del {producto}: ")
    
    elemento ={"artículo" : producto, "precio": float(precio) }
    
    buy_car.update({f"{len(buy_car)+1}": elemento})    
    
def buying_state():
    user_state = input("Escriba 'C' para continuar o 'X' para terminar: ")
    user_state = user_state.lower()
    
    if user_state == "c" or user_state == "x":
        if user_state == "x":
            global state
            state = False
    else:
        print("No se escribió un valor valido")
        buying_state()
        
def return_list():
    total = 0
    for i in buy_car:
        print(f"{buy_car[i].get('artículo','producto').capitalize()} - {round(buy_car[i].get('precio', 0), 2)}")
        total += buy_car[i].get("precio", 0)
                
    print(f"Total - {round(total, 2)}")


while state:
    add_product()
    
    buying_state()
return_list()