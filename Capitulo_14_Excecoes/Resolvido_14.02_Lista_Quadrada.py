def Quadrado(L):
    # if not isinstance(L, list) and not isinstance(L, tuple):
    if not isinstance(L, list | tuple):
        raise TypeError(f"Erro de tipo. O argumento da função Quadrado precisa ser uma lista ou uma tupla. Foi usado {type(L)}.")
    # if all(isinstance(x, int) for x in L or isinstance(x, float) for x in L):
    if not all(isinstance(x, int | float) for x in L):
        raise ValueError("Os elementos de L devem ser todos numéricos.")
    return [i * i for i in L]

Lst = []
a = 30
V = [2, 3, 4, 'texto']
Valor = int(input("Digite um número inteiro diferente de 0 (0 para terminar): "))
while Valor != 0:
    Lst.append(Valor)
    Valor = int(input("Digite um número inteiro diferente de 0 (0 para terminar): "))

print(Quadrado(Lst))
# print(Quadrado(a))
print(Quadrado(V))