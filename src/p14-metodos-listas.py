#dunder methods
lista = [1,2,3,4,5,6,7,8,9,10]
#tamaño del objeto
#print(lista.__dir__())
#print(lista.__len__())

# Muestra una pequeña ayuda de metodo
#help(lista)

print("Método append()")
print("---------------")

#inicializar la variable
colores = []
#Agregamos valores a la lista
#normalmente esto queda dentro de un for
colores.append('verde')
colores.append('rojo')
colores.append('rosa')
colores.append('azul')
print(colores)

print()
print("Método insert()")
print("---------------")


#              0   1   2   3
lista_puntos=[".",".",".","."]
print(lista_puntos)

lista_puntos.insert(2,"-")
print(lista_puntos)

lista_puntos.insert(-2,"*")
print(lista_puntos)


print()
print("Método pop()")
print("---------------")

print(colores)

color_eliminado=colores.pop(2)

print('lista', colores)
print(f"color eliminado: {color_eliminado}")


print()
print("Método remove()")
print("---------------")
# Recibe el valor a eliminar
# Elimina la primer ocurrencia

numeros = [100,400,50,200,50,300]
numero_eliminado=numeros.remove(50)

print('lista', numeros)

print()
print("Método sort() y reverse()")
print("---------------")
# Ordena una lista en orden ascendente
# Modifica la las posiciones de la lista, cuidado

# Reverse invierte el orden actual
numeros.reverse()
print("Lista orden cambiado", numeros)

numeros.sort()
print("lista ordenada[asc]",numeros)

#ordena una lista en orden descendente
numeros.sort(reverse=True)

print("lista ordenada[desc]",numeros)


print()
print("Funcion sorted()")
print("---------------")

numeros_aux = [100,400,50,200,50,300]
lista_ordenada = sorted(numeros_aux)

print("Lista original", numeros_aux)
print("Lista ordenada", lista_ordenada)