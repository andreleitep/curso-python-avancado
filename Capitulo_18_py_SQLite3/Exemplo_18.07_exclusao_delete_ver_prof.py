import sqlite3
from tkinter.messagebox import ERROR

conector = sqlite3.connect('loja.db')
cursor = conector.cursor()

# sql = "delete from produto" --> limpa a tabela (deleta tudo)
sqlCont = "select count(codigo) from produtos where codigo = ?" # count() = função contador (retorna quantidade de ocorrências do parâmetro fornecido)
sqlDel = "delete from produtos where codigo = ?"
codigo = input("Digite o código a ser excluído: ")
excluidos = []
while codigo.upper() != 'FIM':
    try:
        cursor.execute(sqlCont, [int(codigo)])
        cont = cursor.fetchone() # o comando fetchone() recebe uma tupla com todos os parâmetros do count (que poderia ter contado mais do que um parâmetro)
        if cont[0] == 0: # cont tem índice porque ele é uma tupla com apenas um elemento, neste caso
            print(f"Produto {codigo} inexistente")
        else:
            cursor.execute(sqlDel, [int(codigo)]) # o segundo parâmetro sempre tem que ser uma lista
            print(f"Produto {codigo} excluído.")
            excluidos.append(int(codigo))
    except ValueError as e:
        print("Código inválido: ")
        print(e, "\nErro de tipo")
    except sqlite3.OperationalError as e:
        print("Erro operacional: ")
        print(e)


    codigo = input("\nDigite o código a ser excluído: ")

# conector.commit() # --> conclui a exclusão
print('Foram excluídos os produtos: ')
print(excluidos)

cursor.close()
conector.close()