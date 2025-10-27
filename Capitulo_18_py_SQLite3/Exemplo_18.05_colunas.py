import sqlite3
conector = sqlite3.connect('loja.db')
cursor = conector.cursor()

sql = "alter table produtos add custo numeric"
cursor.execute(sql)

sql = "alter table produtos add aliqicms numeric"
cursor.execute(sql)

sql = "alter table produtos add qtdemin integer"
cursor.execute(sql)

sql = "update produtos set custo = 0, aliqicms = 0, qtdemin = 0" # poderia ter where (condição) aqui
cursor.execute(sql)
conector.commit() # Só o update precisa do commit().

cursor.close()
conector.close()
print('\nFim de Programa.')