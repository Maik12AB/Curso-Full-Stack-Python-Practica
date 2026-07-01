efemerides = {
    "1 de Enero": "Año Nuevo",
    "27 de Febrero": "Terremoto en Chile",
    "8 de Marzo": "Día de la Mujer",
    "21 de Mayo": "Glorias Navales",
    "18 de Septiembre": "Fiestas Patrias",
    "19 de Septiembre": "Glorias del Ejercito",
    "25 de Diciembre": "Navidad",
}

fecha = input("Ingrese una fecha: ")
efe = efemerides.get(fecha,"ND")
print(efe)

if efe =="ND":
    print("No existe efemerides para esta fecha")
    print(f"El usuario ha ingresado: {fecha}")
else:
    print(efe)