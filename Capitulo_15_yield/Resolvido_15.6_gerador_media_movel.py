def media_movel():      # Minha primeira tentativa foi iniciar uma lista
    total = qtde = 0    # mas é justamente o que não precisa neste caso, se não, eu vou gerar uma lista infinita
    while True:
        novo_dado = (yield total / qtde if qtde > 0 else 0)
        if novo_dado is not None:
            total += novo_dado
            qtde += 1

#programa principal
gen = media_movel()
next(gen)
numero = input("Forneça um número (ou FIM para encerrar): ")
while numero.upper() != "FIM":
    resultado = gen.send(float(numero))
    print(f'média móvel atual = {resultado:.3f}')
    numero = input("Forneça um número (ou FIM para encerrar): ")

print('\nFim do programa.')