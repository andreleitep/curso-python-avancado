texto = "Neste módulo as funções imprimem um texto"

def paridade(valor):
    """Imprime PAR ou ÍMPAR conforme o valor passado"""
    if valor % 2 == 0:
        print(f"{valor} é PAR")
    else:
        print(f"{valor} é ÍMPAR")

def primo(valor):
    """Imprime PRIMO ou NÃO-PRIMO conforme o valor passado"""
    if valor == 2:
        print(f"{valor} é PRIMO")
    elif valor % 2 == 0:
        print(f"{valor} é NÃO-PRIMO")
    else:
        raiz = valor ** 0.5
        teste = resto = 3
        while teste < raiz and resto != 0:
            resto = valor % teste
            teste += 2
        if resto != 0:
            print(f"{valor} é PRIMO")
        else:
            print(f"{valor} é NÃO-PRIMO")