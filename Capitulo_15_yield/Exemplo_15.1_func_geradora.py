def gera_simples():
    yield 38
    yield 159
    yield 47
    yield 26

gerador = gera_simples()
print('gera_simples =', type(gera_simples))
print('gera_simples() =', type(gera_simples()))
print('gerador =', type(gerador))
print('gerador 1:')
for valor in gerador:
    print(valor)

print('gerador 2:')
for valor in gera_simples():
    print(valor)

