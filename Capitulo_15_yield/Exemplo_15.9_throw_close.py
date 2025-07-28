def simples():
    num = 10
    while True:
        yield num
        num += 10

gen = simples()
# for i in range(5):
#     print(next(gen))

# esta parte do programa só é possível testar no Idle
# gen.throw(Exception('Gerador terminado pelo usuário'))
# print(next(gen))

# for valor in gen:
#     if valor > 70:
#         gen.throw(ValueError("Todos os valores de interesse já foram gerados."))
#     print(valor)

# gen.close()
# next(gen)

for valor in gen:
    if valor > 70:
        gen.close()
    print(valor)

print("Fim do programa")