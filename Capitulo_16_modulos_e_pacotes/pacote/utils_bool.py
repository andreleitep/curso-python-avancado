texto = ('Neste módulo as funções retornam um booleano')

def paridade(valor):
    """Retorna True se o valor for par, e False se for ímpar"""
    if valor % 2 == 0:
        return True
    else:
        return False

def primo(valor):
    """Retorna True se o valor for primo, e False se não for"""
    if valor == 2:
        return True
    elif valor % 2 == 0:
        return False
    else:
        raiz = valor ** 0.5
        teste = 3
        while teste <= raiz:
            if valor % teste == 0:
                return False
            teste += 2
        return True

