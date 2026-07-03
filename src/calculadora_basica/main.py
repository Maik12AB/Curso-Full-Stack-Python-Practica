import sumar

def restar(x,y):
    print(f"El resultado de la resta es: {x - y}")

def tomar_datos():
    x = int(input("Ingrese el primer numero: "))
    y = int(input("Ingrese el segundo numero: "))
    return x, y

print("Calculadora basica")
print("--------------------\n")
print("Que operacion le gustaria realizar?")
print("1. Sumar dos numeros")
print("2. Restar dos numeros")
print("0. Salir")

opcion = input("> ")
#Realizamos esta refactorizacion para tener un solo punto de ingreso de datos
#Mas adelante vamos a cambiar la funcion de tomar_datos()
if opcion in ("1","2"):
    x, y = tomar_datos()
    if opcion =="1":
        sumar.sumar(x,y)
    elif opcion =="2":
        restar(x,y)
elif opcion =="0":
    print("Nos vemos a la proxima")
else:
    print("No existe la opcion ingresada")