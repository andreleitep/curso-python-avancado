class Attr:
    attrclasse = 9.99
    def __init__(self, num, txt):
        self.num = num
        self.txt = txt
    def exibedados(self):
        self.outro = 999
        print(f'attrclasse = {self.attrclasse}\n' +
              f'num = {self.num}\n' +
              f'txt = {self.txt}\n' +
              f'outro = {self.outro}')

objA = Attr(10, 'Texto do Objeto A')
objB = Attr(20, 'Texto do Objeto B')
objA.exibedados()
print('\n',objA.num)
print()
print(objA.attrclasse)
print()
print('attrclasse alterado')
print()
Attr.attrclasse = 1250
objA.exibedados()
print()
objB.exibedados()