# Funções geradoras são boas para casos que precisamos de valores cumulativos
def funcao_fatorial():
    num, fat = 0, 1
    while True:
        dado = (yield num, fat)
        num += 1
        fat *= num
        if dado is not None:
            num = dado[0]
            fat = dado[1]

# Programa principal

B = input("Digite dois números, um base e seu fatoria separado por espaço: ")
dupla = B.split()
dupla[0] = int(dupla[0])
dupla[1] = int(dupla[1])
dupla = tuple(dupla)
A = int(input("Digite a quantidade: "))
ger_fat = funcao_fatorial()
next(ger_fat)
ger_fat.send(dupla)
print(dupla)
for i in range(A-1):
    print(next(ger_fat))
print("\nFim do programa")