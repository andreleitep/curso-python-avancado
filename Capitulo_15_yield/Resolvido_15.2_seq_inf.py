# Funções geradoras são boas para casos que precisamos de valores cumulativos
def funcao_fatorial():
    num, fat = 0, 1
    while True:
        yield num, fat
        num += 1
        fat *= num

# Programa principal

A = int(input("Digite a quantidade: "))
ger_fat = funcao_fatorial()
for i in range(A):
    print(next(ger_fat))
print("\nFim do programa")