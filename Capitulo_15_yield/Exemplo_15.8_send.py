def fg(): # Função Geradora
    resto = 0
    num = 2
    while True:
        if num % 2 == resto:
            dado = (yield num)
            if dado is not None: # Essa parte só executa quando eu usar o método send
                if dado not in (0, 1):
                    raise ValueError(f"Esperado 0 ou 1 - passado {dado}")
                resto = dado
                num = 0
        num += 1



gen = fg()
print("Gera 5 valores pares")
for _ in range(5):
    print(next(gen), end=' ') # dado recebe None

print("\nSua escolha!")
qual = int(input("0 ou 1? "))
ret = gen.send(qual) # dado recebe o valor da variável "qual", ret recebe valor de "qual"?
print(ret, end=' ')
for _ in range(4):
    print(next(gen), end=' ')

'''
print("\nGera 7 valores pares")
ret = gen.send(0)
print(ret, end=' ')
for _ in range(7):
    print(next(gen), end=' ')
'''

# ret = gen.send(2)