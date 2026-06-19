#comentarios
print("Hola Mundo")
'''
comentario
de
varias
lineas
'''
'''
Trabajando con variables
-Nombre: iniciar con una letra o un guion bajo
-Valor
-Tipo de dato
'''
nombre = "Maikol"
print(nombre)

print("Tipo de dato de la variable nombre: ", type(nombre))
#ejemplos concatenacion
'''
print("Maikol", "Acuña")
print("Maikol" + "Acuña")
'''
# Metodos en variables
print(nombre.upper())

# Asignar tipo de dato
apellido:str = "Acuña"
print(apellido)
# Cambiar valor(otro tipo de dato) de una variable
apellido = 10
print(apellido, type(apellido))

# Posicion de memoria de una variable
print(id(apellido))

# Tipo de dato numericos
edad = 25
print("Edad:", edad, type(edad))



# Comportamiento de numeros enteros
numero_entero1=10
numero_entero2=20
print("Suma de numeros enteros:", numero_entero1 + numero_entero2)
print("Resta de numeros enteros:", numero_entero1 - numero_entero2)
print("Multiplicacion numeros enteros:", numero_entero1 * numero_entero2)
#La division retorna un dato de tipo float
print("Division", 7 / 2, type(7/2))
print("Division", 2 // 2, type(2//2))

#La division doble retorna un dato de tipo int
print("Division(int)", 7 // 2, type(7//2))
print("Division(int)", 2 // 2, type(2//2))

# El modulo es el resto de la division(retorna int)
print("Division(int)", 7 % 2, type(7%2))
print("Division(int)", 2 % 2, type(2%2))

# Caso de uso
elementos = 33
por_pagina = 10
print("Tenemos", elementos//por_pagina, "paginas")

#saber si un numero es par o impar
if (10 % 2) == 0:
    print("El numero es par")
else:
    print("El numero es impar")


n1="10"
n2="20"
print("Concatenando n1+n2", n1+n2)

print()
print("Sumar dos numeros")
print("--------------------")
primer_numero=input("Ingrese el primer numero: ")
segundo_numero=input("Ingrese el segundo numero: ")

print("La suma de los dos numeros es: ", primer_numero + segundo_numero)

print("La suma de los dos numeros es: ", int(primer_numero) + int(segundo_numero))

#usando f string
suma_str = f"La suma de {primer_numero} con {segundo_numero} es: {int(primer_numero) + int(segundo_numero)}"
print(suma_str)