class Exemplo:
    fruta = 'Laranja'
    cor = 'azul'
    def __init__(self, valor):
        self.valor = valor

obj1 = Exemplo(125)
obj2 = Exemplo(3.75)

print(obj1.__dict__) # {'valor': 125}  ──> não aparecem no dicionário do objeto
print(obj2.__dict__) # {'valor': 3.75} └─> os atributos da classe "fruta" e "cor"

print(obj1.cor)
print(obj1.fruta)
print(obj2.cor)
print(obj2.fruta)

for s in Exemplo.__dict__.items():
    print(s)