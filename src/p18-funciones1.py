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

numero1 = input("Ingrese el primer número entero:")
numero2 = input("Ingrese el segundo número entero:")

if not es_entero(numero1):
    msj_error("Primero", numero1)

if not es_entero(numero2):
    msj_error("Segundo", numero2)

if numero1.isdigit() and numero2.isdigit():
    numero_1 = int( numero1 )
    numero_2 = int( numero2 )

    suma = numero_1 + numero_2