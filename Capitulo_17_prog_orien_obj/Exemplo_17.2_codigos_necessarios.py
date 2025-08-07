class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calc_area(self):
        return self.base * self.altura

    def exibe(self):
        print(f'Retângulo ({self.base} x {self.altura})')
        print(f'    área = {self.calc_area()}')

r1 = Retangulo(12, 5)
print('r1: ', end='')
r1.exibe()

r2 = Retangulo(3.5, 9.0)
print('\nr2: ', end='')
r2.exibe()

r2.base = 9.5
r2.altura = 16.3
area = r2.calc_area()
print(f'\nNovas medidas de r2: base = {r2.base} - altura = {r2.altura}')
print(f'Área do retângulo r2, com as novas medidas = {r2.calc_area()}')