import csv
from p24_poo_clase_medicamento import Medicamento


def main():
    # Imprimir encabezado
    print("------------------------------------")
    print("Importando medicamentos desde el csv")
    print("------------------------------------", "\n")
    # Importar archivo csv
    items = []
    with open("src/data/medicamentos.csv", "r") as f:
        contenido = csv.reader(f)
    # Procesar archivo csv
        for item in contenido:
            items.append(item)
    
    # Imprimir cada medicamento con las reglas de la clase medicamento
    for i, v in enumerate(items) :
        if i == 0:
            t = f"{v[0]} {v[1]} {v[2]}"
            print(t)
            print('-'*len(t))
        else:
            stock = v[1]
            if stock == 'null':
                stock = 0
            else:
                stock = int(stock)

            precio = int(v[2])
            o = Medicamento(v[0], stock)
            o.asignar_precio(precio)
            print(f"{o.nombre}, {o.stock}, {o.descuento},{o.precio_neto},{o.precio_neto}, {o.precio_bruto}")

if __name__ == '__main__':
    main()