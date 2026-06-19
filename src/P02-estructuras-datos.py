print("Estructuras de datos en Python") 
print("==============================\n")


# Listas
print("Listas (list)")
print("-------------")

# Indice       0        1         2          3
# Negativo     -4     -3         -2         -1
fullstack = ["HTML", "CSS", "Javascript", "Python"]
print(fullstack)

print(f"El tipo de dato es: {type(fullstack)}")

# Acceder a un elemento de una lista 
print(fullstack[2]) #Javascript
#print(fullstack[10]) #error list index out of range
print(fullstack[-1])#python

# Agregar elementos a una lista
fullstack.append("Base de datos")
#Cambiar valor
fullstack[3] = "Python 3.13"

print(fullstack)







#------------------------------------------------------------------
# Tuplas
titulo = "Tuplas (tuples) esto es un ejemplo dinamico de repetir caracteres"
print(titulo)
print("-"* len(titulo))

curso = ("Bootcamp", "Fullstack", "Python", "2026")

print(curso)
print(f"El tipo de dato es: {type(curso)}")
print()




# Set

titulo = "Set(set)"
print(titulo)
print("-"* len(titulo))


lenguajes = {"Python", "Javascript", "PHP", "C#", "Elixir", "Java", "Python", "Python" }
print(lenguajes)
print(f"El tipo de dato es: {type(lenguajes)}")


lista_duplicada = [1,2,3,4,1,6,1]
print(set(lista_duplicada))
# Diccionarios