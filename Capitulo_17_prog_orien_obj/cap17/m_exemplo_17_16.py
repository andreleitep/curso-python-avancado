class NumeroPositivo:
    def __set_name__(self, owner, name):
        self._name = name
    def __get__(self, obj, objtype=None):
        return obj.__dict__[self._name]
    def __set__(self, obj, value):
        if not isinstance(value, int | float):
            raise TypeError('Valor numérico esperado')
        if value < 0:
            raise ValueError('Valor positivo esperado')
        obj.__dict__[self._name] = value

class Retangulo:
    base = NumeroPositivo()
    altura = NumeroPositivo()

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calc_area(self):
        return self.base * self.altura

    def exibe(self):
        print(f' Retângulo ({self.base} x {self.altura})')
        print(f'      Área  {self.calc_area():.3f}')