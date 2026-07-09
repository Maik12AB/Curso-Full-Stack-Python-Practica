#Quiero que mi metodo de sumar() reciba los 
# argumentos directamente o quiero que los 
# lea desde los atributos de la clase?

# metodo no estatic
class CalculadoraNoStatic():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def sumar(self):
        return self.a + self.b

# metodo static
class CalculadoraStatic():
    @staticmethod
    def sumar(a,b):
        return a + b

class CalculadoraMix():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def sumar(self):
        return self.a + self.b




calc = CalculadoraNoStatic(10,20)
print(calc.sumar())

calc_static = CalculadoraStatic()
print(calc_static.sumar(10,20))

