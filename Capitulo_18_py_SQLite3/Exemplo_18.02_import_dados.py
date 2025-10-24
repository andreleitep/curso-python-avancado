import sqlite3

conector = sqlite3.connect('loja.db')
cursor = conector.cursor()

try:
    sql = "drop table produtos"
    cursor.execute(sql)
except sqlite3.OperationalError:
    pass

sql = """
        create table produtos
        (codigo integer, descr text, preco numeric, qtdeestq integer)
"""
cursor.execute(sql)

sql = """
        insert into produtos (codigo, descr, preco, qtdeestq)
        values (?, ?, ?, ?)
"""
nome_arq = 'I:\Meu Drive\ADS - FATEC\Outros Cursos\python-avancado\Capitulo_18_py_SQLite3\Cap18\papelaria.txt'
for linha_arq in open(nome_arq, 'r', encoding='utf-8'):
    dados = linha_arq.split(';')
    print(dados)
    # cursor.execute(sql, [1251, 'Papel Sulfite A4, 100 folhas', 7.25, 188])
    cursor.execute(sql, dados)
    # Não precisa converter, a conversão de dados é automática pela definição inicial da tabela
    # Também não precisa retirar o '\n' do final das linhas


conector.commit()
cursor.close()
conector.close()

print('\nFim do Programa.')