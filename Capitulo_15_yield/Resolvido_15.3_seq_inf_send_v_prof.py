# Funções geradoras são boas para casos que precisamos de valores cumulativos
def funcao_fatorial():
    num, fat = 0, 1
    while True:
        i = (yield num, fat)
        num += 1
        fat *= num
        if i is not None:
            num, fat = i, 1
            for a in range(1, num+1):
                fat *= a

qtde = int(input("Digite a quantidade: "))
gen = funcao_fatorial()
next(gen)
prim = int(input("\nValor inicial: "))
while prim >= 0:
    r = gen.send(prim)
    fatoriais = [r]
    for _ in range(qtde-1):
        fatoriais.append(next(gen))
    print(f"\nSequência de fatoriais iniciando em {prim}")
    print(fatoriais)

    prim = int(input("\nValor inicial: "))