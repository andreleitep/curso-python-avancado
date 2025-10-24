import sqlite3
conector = sqlite3.connect('loja.db')

cursor = conector.cursor()

sql = """
      create table produto
      (codigo integer, descr text, preco numeric, qtdeestq integer)
      """
cursor.execute(sql)

sql = """
      insert into produto (codigo, descr, preco, qtdeestq)
      values (1138, 'lápis preto', 1.90, 376)
      """
cursor.execute(sql)

sql = """
      insert into produto (codigo, descr, preco, qtdeestq)
      values (1251, 'Papel Sulfite A4, 100 folhas', 7.25, 188)
      """
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print('\nFim do programa.')