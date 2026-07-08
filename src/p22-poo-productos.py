class Producto():
    #Cuando se requiere  enviar valores a la clase, 
    # la definicion debe estar en el constructor
    # en pyhton el constructor es un metodo
    # __init__(self)
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.error = ''

    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio

    def get_stock(self):
        return self.stock
    
    def vender(self, u:int):
        if self.stock < u:
            self.error = "No tenemos unidades suficientes"
            return False
        
        self.stock -= u
        return True

pelota = Producto("Pelota de futbol", 20, 5)
print('-'*30)
print(f"Nombre del producto: {pelota.get_nombre()}")
print(f"Precio del producto: {pelota.get_precio()}")
print(f"Stock disponible: {pelota.get_stock()}")

unidades = int(input("Unidades a ser vendidas: "))

if pelota.vender(unidades):
    print("Venta realizada con exito")
else:
    print(f"No se puede realizar la venta por -> {pelota.error}")

print('-'*30)
print(f"Nombre del producto: {pelota.get_nombre()}")
print(f"Precio del producto: {pelota.get_precio()}")
print(f"Stock disponible: {pelota.get_stock()}")