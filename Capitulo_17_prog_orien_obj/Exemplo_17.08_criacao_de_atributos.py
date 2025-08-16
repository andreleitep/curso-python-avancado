from cap17 import funcoes_uteis

class Produto:
    def __init__(self, nome, codbarras):
        self.nome = nome
        self.codbarras = codbarras
        self.estq = 0
    def atr_custo(self, custo):
        self.custo = custo
    def exibe(self):
        print(f'Produto: {self.nome} ({self.codbarras})')
        print(f'   └─> Estoque: {self.estq}')
        if hasattr(self, 'custo'):
            print(f'   └─> Preço de Custo: {self.custo}')

maca = Produto('Maçã', '1234567891234')
maca.exibe()
# maca.custo = 13.79 ──> funciona também
maca.atr_custo(15.85)
maca.exibe()

funcoes_uteis.ba()

print('dir(maca):')
funcoes_uteis.exibe_lista(dir(maca))
print('maca.__dict__')
funcoes_uteis.exibe_lista(maca.__dict__)

funcoes_uteis.ba()

print('dir(Produto)')
funcoes_uteis.exibe_lista(dir(Produto))
print('Produto.__dict__')
funcoes_uteis.exibe_lista(Produto.__dict__)