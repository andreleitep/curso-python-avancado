# Nesta aula, o professor faz um tratamento de erros incompleto.

import sqlite3
conector = sqlite3.connect('loja.db')
cursor = conector.cursor()

sql = """
        insert into produtos (codigo, descr, preco, qtdeestq)
        values (?, ?, ?, ?)
"""

print('Digite os dados separados por vírgulas')
print('Código,Descrição,Preço,Estoque')
Ler = input()
while Ler != '':
    # 25010, produto 25010, 25.39, 189
    try:
        dados = Ler.split(',')
        i = 0
        for d in dados:
            dados[i] = d.strip()
            print(dados[i], sep=' - ')
            i+=1
        cursor.execute(sql, dados)
        conector.commit()
    except sqlite3.OperationalError as e:
        print(e.sqlite_errorname)
        print(f'{dados} Dados inválidos')
    else:
        print(' ' * 10, '... dados inseridos com sucesso')
    finally:
        print('Código,Descrição,Preço,Estoque')

    Ler = input()

cursor.close()
conector.close()

print('\nFim do Programa.')