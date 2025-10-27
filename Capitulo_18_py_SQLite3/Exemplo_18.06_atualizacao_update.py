import sqlite3
conector = sqlite3.connect('loja.db')
cursor = conector.cursor()

for linha in open('cap18\\papelaria_atualiz.txt', 'r', encoding='utf-8'):
    dados = linha.split(';')
    dados = [dado.strip() for dado in dados]
    ult = dados.pop(0)
    dados.append(ult)
    print(dados)
    sql = """
            update produtos
                set custo = ?, aliqicms = ?, qtdemin = ?
                where codigo = ?
    """
    cursor.execute(sql, dados)
conector.commit()
print('Tabela atualizada.')

cursor.close()
conector.close()
print('\nFim do Programa.')