from cap17.funcoes_uteis import ba, exibe_lista


class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor
    def __fazalgo(self):
        print(f'valor = {self.valor} em método fazalgo')
    def exibevalor(self):
        print(f'valor = {self.valor} em método exibevalor')

lista = [2, 4, 6, 8]
i = 1
exibe_lista(dir(MinhaClasse))

ba()

class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor
    def _fazalgo(self):
        print(f'valor = {self.valor} em método fazalgo')
    def exibevalor(self):
        print(f'valor = {self.valor} em método exibevalor')

lista = [2, 4, 6, 8]
i = 1
exibe_lista(dir(MinhaClasse))

ba()

class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor
    def __fazalgo__(self):
        print(f'valor = {self.valor} em método fazalgo')
    def exibevalor(self):
        print(f'valor = {self.valor} em método exibevalor')

lista = [2, 4, 6, 8]
i = 1
exibe_lista(dir(MinhaClasse))
