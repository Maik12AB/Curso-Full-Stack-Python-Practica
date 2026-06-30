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
