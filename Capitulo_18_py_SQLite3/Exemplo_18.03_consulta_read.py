import sqlite3
conector = sqlite3.connect('loja.db')
cursor = conector.cursor()

sql = """ 
        select * from produtos 
        where codigo >= 11000 and codigo <= 11999 
        order by codigo desc
      """
        # retorna todas as colunas (se quiser retornar 2 colunas, substituir * por 'preco, nome')
cursor.execute(sql)

dados = cursor.fetchall()

cursor.close()
conector.close()

print('\nConsulta ao Banco de Dados "loja.db" \n')
print('Dados da tabela "produtos"')
print('-' * 61)
print("{:<7}{:^40}{:>8}{:>6}".format('Código', 'Descrição', 'Preço', 'Estq'))
print('- ' * 31)
for d in dados:
    print("{:<7}{:40}{:>8.2f}{:6}".format(d[0],d[1],d[2],d[3]))
print("-" * 61)
print(f"Encontrado(s) {len(dados)} registro(s).")
print('\n\nFim do Programa.')