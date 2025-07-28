def fg(): # Função Geradora
    resto = 0
    num = 2
    while True:
        if num % 2 == resto:
            dado = (yield num)
            if dado is not None:
                if dado not in (0, 1):
                    raise ValueError(f"Esperado 0 ou 1 - passado {dado}")
                resto = dado
                num = 0
        num += 1

gen = fg()
print("Gera 5 valores pares")
for _ in range(5):
    print(next(gen), end=' ')

print("\nGera 5 valores ímpares")
ret = gen.send(1)
print(ret, end=' ')
for _ in range(4):
    print(next(gen), end=' ')

print("\nGera 7 valores pares")
ret = gen.send(0)
print(ret, end=' ')
for _ in range(7):
    print(next(gen), end=' ')

ret = gen.send(2)