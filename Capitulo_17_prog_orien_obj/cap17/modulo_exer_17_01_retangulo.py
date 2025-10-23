class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        print(self.base, "x", self.altura, "=", f'{self.base * self.altura:.3f}')