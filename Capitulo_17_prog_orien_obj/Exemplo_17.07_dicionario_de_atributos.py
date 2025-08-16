# Para testar no Idle

from cap17.funcoes_uteis import exb_lst_n_prvd, ba

class Exemplo:
    def __init__(self, dado):
        self.dado = dado
    def calculo(self):
        a = 10
        self.b = 5
        self.c = 2
        return self.dado

obj = Exemplo(23)
exb_lst_n_prvd(dir(obj))

ba()

print(obj.calculo())

exb_lst_n_prvd(dir(obj))