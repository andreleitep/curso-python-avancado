def filtro(dados, pmin, pmax):
    for valor in dados:
        if pmin <= valor <= pmax:
            yield valor, valor * 1.1 # retorna tupla

precos = [36.3, 174.19, 43.71, 108.32, 89.14]
lmin = int(input("Determine o mínimo: "))
lmax = int(input("Determine o máximo: "))
for valores in filtro(precos, lmin, lmax):
    print(valores)

print('\nFim do programa')