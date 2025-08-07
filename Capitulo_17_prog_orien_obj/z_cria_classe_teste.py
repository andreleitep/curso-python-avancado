class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calc_area_tri(self):
        return (self.base * self.altura) / 2

    def exibe(self):
        print(f'base = {self.base}, altura = {self.altura}')
        print(f'    área = {self.calc_area_tri()}')

# programa principal
tri1 = Triangulo(5, 3)
print('tri1: ', end='')
tri1.exibe()