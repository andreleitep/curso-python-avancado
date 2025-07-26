def le_arquivo(nome_arq):
    for uma_linha in open(nome_arq, 'r'):
        uma_linha = uma_linha.split(';')
        # yield uma_linha.rstrip()
        yield uma_linha[0], int(uma_linha[3]) # retorna uma tupla com a placa e a kilometragem
arquivo = input("Digite o nome do arquivo: ")
for linha in le_arquivo(arquivo):
    print(linha)

print("\nFim do programa")