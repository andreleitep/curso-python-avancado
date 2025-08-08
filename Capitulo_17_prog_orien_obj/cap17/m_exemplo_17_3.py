class Veiculo:
    def __init__(self, placa, modelo, ano, km):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.km = km

    def exibe(self):
        print(f'│{f' Veículo placa {self.placa}':<60}│')
        print(f'│{f'     modelo {self.modelo}, ano {self.ano}, kilometragem {self.km}':<60}│')