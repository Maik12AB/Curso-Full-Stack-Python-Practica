print()
print("Agregar elementos a un diccionario(dict)")
print("----------------------------------------")

#Cuando hacemos referencia a la clave de un dict que no existe, la agrega

diccionario = {"llave1": 5}

print(diccionario)

diccionario["llave2"] = 9

print(diccionario)

print()
print("Cambiar valor de una clave de un diccionario(dict)")
print("----------------------------------------")

diccionario["llave2"] = 18

print(diccionario)

print()
print("eliminar elementos")
print("----------------------------------------")


diccionario = {"celular": 140000, "notebook": 489990, "tablet": 120000, "cargador": 12400}
print("Diccionario original", diccionario)

#motodo pop()
# Elimina un elemento de un dict usando la clave 'key' y devuelve el valor

valor_eliminado = diccionario.pop("celular")
print("Eliminado 'celular'", diccionario)
print(f"valor de 'celular'= {valor_eliminado}")

print()
print("Actualizar diccionarios")
print("----------------------------------------")

diccionario_a = {"nombre": "Alejandra", "apellido": "López", "edad": 33, "altura": 1.55}
diccionario_b = { "mascota":"miti", "ejercicio":"bicicleta"}

diccionario_a.update(diccionario_b)
print("Diccionario actualizado", diccionario_a)

diccionario_c = {"edad":40}
diccionario_a.update(diccionario_c)

print("Diccionario actualizado", diccionario_a)


print()
print("Metodo 'keys()'")
print("----------------------------------------")

#Devuelve las claves de un diccionario
# El objeto devuelto se puede:
# - Iterar
# - Validar contenido
# Esta enlazado dinamicamente
llaves = diccionario.keys()
print(llaves)

#validar si existe una llave
for aux in llaves:
    print(aux)
if "celular" not in llaves:
    print("No existe la llave de ['celular']")
    print("Actualizando diccionario")
    diccionario["celular"] = 140_000
print("nuevo diccionario", diccionario)
print("la variable llaves se actualiza dinamicamente", llaves)    


print()
print("Metodo 'value()'")
print("----------------------------------------")

#Comportamiento similar a 'keys'
valores = diccionario.values()
print(valores)

print()
print("Metodo 'items()'")
print("----------------------------------------")

#comportamiento similar a keys() y values()
#Regresa una tupla

lista = diccionario.items()
print(lista)

for clave,valor in diccionario.items():
    print(f"-{clave}:{valor}")
