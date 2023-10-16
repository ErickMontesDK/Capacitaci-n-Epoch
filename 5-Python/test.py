#variables
variable = 1

#constante
CONSTANTE = "Texto"

#Tipos de datos
    #Cadena de texto (string):
mi_cadena = "Hola Mundo!"

mi_cadena_multilinea = """
Esta es una cadena
de varias lineas
"""
#CASTING
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get data Type
x = 5
y = "John"
print(type(x))
print(type(y))

#Multiples variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Un valor a muchas variables
x = y = z = "Orange"
#Unpack collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

#Variables globales
ax = "awesome"

def myfunc():
    global ax
    ax = "fantastic"

myfunc()

print("Python is " + ax)



#Random
import random
random.randrange(1, 10)

#Tipos de datos
x = str("Hello World") 
x= "Hello World"	

x = int(20)		
x=20

x = float(20.5)	
x=20.5

x = complex(1j)		
x=1j

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

x = list(("apple", "banana", "cherry"))	
x=["apple", "banana", "cherry"]	

x = tuple(("apple", "banana", "cherry"))
x = ("apple", "banana", "cherry")

x = range(6)	

x = dict(name="John", age=36)	
x={"name":"John", "age":36}	

x = set(("apple", "banana", "cherry"))	
x = {"apple", "banana", "cherry"}

x = frozenset(("apple", "banana", "cherry"))

x = bool(5)		
x = True

x = bytes(5)
x = b"Hello"	

x = bytearray(5)

x = memoryview(bytes(5))	

x= None

## slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])