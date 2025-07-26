def gerador_pares(): # O gerador infinito não interrompe sua execução, os objetos utilizam os valores gerados antes
    a = 2
    while True:
        yield a
        a += 2

gen = gerador_pares()

for a in range(20):
    print(next(gen), end=' ')
print()
gen2 = gerador_pares()

for i in range(6):
    print(next(gen2), end=' ')
print()
for a in range(10):
    print(next(gen), end=' ')
print()
for i in range(24):
    print(next(gen2), end=' ')