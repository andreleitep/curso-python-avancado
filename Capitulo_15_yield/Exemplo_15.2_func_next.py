def gera_simples():
    print('   ... próximo valor retornado = 38')
    yield 38
    print('   ... próximo valor retornado = 159')
    yield 159
    print('   ... próximo valor retornado = 47')
    yield 47
    print('   ... próximo valor retornado = 26')
    yield 26

gerador = gera_simples()

g1 = next(gerador) # executa tudo o que está acima do yield em questão
print(g1)
print(next(gerador))