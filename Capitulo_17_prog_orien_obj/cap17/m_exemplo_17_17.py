class FormaGeometrica:
    def __init__(self):
        self.tipo_forma = 'forma não definida'

    def exibe_tipo_forma(self):
        print(self.tipo_forma)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.tipo_forma = 'Círculo'
        self.raio = raio

    def exibe_dados(self):
        super().exibe_tipo_forma()
        print(f'    detalhes: raio = {self.raio}')


class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.tipo_forma = 'Retângulo'
        self.base = base
        self.altura =  altura

    def exibe_dados(self):
        super().exibe_tipo_forma()
        print(f'    detalhes:'
              f'       base   = {self.base}'
              f'       altura = {self.altura}')
