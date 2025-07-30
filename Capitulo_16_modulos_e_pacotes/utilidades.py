texto = 'Este é o módulo utilidades.py'
texto2 = 'Algo mais'

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
         'jul', 'ago', 'set', 'out', 'nov', 'dez']

def paridade(valor):
    """Retorna PAR ou ÍMPAR conforme o valor passado"""
    if valor % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'

def primo(valor):
    """Se valor for primo retorna True, se não retorna False"""
    if valor == 2:
        return True # 2 é primo
    elif valor % 2 == 0:
        return False # Pares acima de 2 não são primos
    else:
        raiz = valor ** 0.5 # define raiz quadrada de valor
        i = 3 # contador que vai testar o valor (sobe de 2 em 2 para se manter ímpar)
        while i <= raiz: # só testa os valores que estão abaixo da raíz do valor
            if valor % i == 0: # teste do valor
                return False
            i += 2 # sobe de 2 em 2
        return True

"""
--- Buscando no idle ---
import os           ---> operational system
os.getcwd()         ---> current work directory (mostra a pasta em que o python está trabalhando)
os.chdir('Caminho\da\pasta')
"""