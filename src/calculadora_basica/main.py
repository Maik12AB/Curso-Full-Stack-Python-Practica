#import sumar   
#    Modulo       Funcion
from sumar import sumar
from restar import restar

def tomar_datos():
    x = int(input("Ingrese el primer numero: "))
    y = int(input("Ingrese el segundo numero: "))
    return x, y

opcion = ""
while opcion != "0":
    print("Calculadora basica")
    print("--------------------\n")
    print("Que operacion le gustaria realizar?")
    print("1. Sumar dos numeros")
    print("2. Restar dos numeros")
    print("0. Salir")

    opcion = input("> ")
    if opcion == "0":
        print("Nos vemos a la proxima")
        break
        print()
    elif  opcion not in ("1", "2"):
        print("No existe la opcion ingresada")
        continue

    x, y = tomar_datos()
    if opcion =="1":
        resp=sumar(x,y)
        print(f"El resultado de la suma es: {resp}")
    elif opcion =="2":
        resp=restar(x,y)
        print(f"El resultado de la resta es: {x - y}")