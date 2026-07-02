import sys
# Codigo original: src/sumar-dos-numeros.py
# Hacemos que trabaje con funciones
# Refactorizacion
# -Validacion del valor ingresado
# - Mensaje de error

# La funcion valida si un valor es de tipo entero(int)
# REtorno de tipo booleano
# -Entero = true
def es_entero(valor):
    return valor.isdigit()

def msj_error(texto,valor_error):
    print( "Error!!!!" )
    print( "Los valores ingresados deben ser números enteros" )
    print( f"{texto} numero es:  [{valor_error}]" )

def sumar(n1,n2):
    return n1 + n2

numero1 = input("Ingrese el primer número entero:")
numero2 = input("Ingrese el segundo número entero:")

if not es_entero(numero1):
    msj_error("Primero", numero1)
    sys.exit()
if not es_entero(numero2):
    msj_error("Segundo", numero2)
    sys.exit()

numero_1 = int( numero1 )
numero_2 = int( numero2 )

suma = sumar(numero_1, numero_2)

print(f"La suma de los numeros es: {suma}")