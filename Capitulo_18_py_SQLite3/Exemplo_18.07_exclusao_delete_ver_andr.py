import sqlite3
from tkinter.messagebox import ERROR

conector = sqlite3.connect('loja.db')
cursor = conector.cursor()

# sql = "delete from produto" --> limpa a tabela (deleta tudo)
sql = "delete from produtos where codigo = ?"
codigo = input("Digite o código a ser excluído: ")
excluidos = []
while codigo.upper() != 'FIM':
    try:
        sql_busca = "select codigo from produtos"
        cursor.execute(sql_busca)
        codigos_prod = cursor.fetchall()
        cod_prod = [tupla[0] for tupla in codigos_prod]
        print(cod_prod)
        if int(codigo) not in cod_prod:
            print(f"Produto {codigo} inexistente")
        else:
            cursor.execute(sql, [int(codigo)]) # o segundo parâmetro sempre tem que ser uma lista
            print(f"Produto {codigo} excluído.")
            excluidos.append(int(codigo))
    except ValueError as e:
        print("Código inválido: ")
        print(e, "\nErro de tipo")
    except sqlite3.OperationalError as e:
        print("Erro operacional: ")
        print(e)


    codigo = input("\nDigite o código a ser excluído: ")

conector.commit()
print('Foram excluídos os produtos: ')
print(excluidos)

cursor.close()
conector.close()