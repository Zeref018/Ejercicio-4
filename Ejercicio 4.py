class Rectangulo():
    def __init__(self):
        self.base = int(input('dime la base del rectángulo: '))
        self.altura = int(input('dime la altura del rectángulo: '))
    def calcularPerimetro(self):
        print(f'el perimetro es {(self.base * 2) + (self.altura * 2)}')

    def calcularArea(self):
        print(f'el area es {self.base * self.altura}')


rectangulo1 = Rectangulo()
rectangulo1.calcularPerimetro()
rectangulo1.calcularArea()