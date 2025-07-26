def Primo(V):
    '''Se V for primo, retorna True, senão retorna False'''
    if not isinstance(V, int):
        raise TypeError('Tipo inválido. O argumento deve ser um número inteiro.')
    if V < 2:
        raise ValueError('Valor inválido. O argumento deve ser no mínimo 2.')
    if V == 2:
        return False
    elif V % 2 == 0:
        return False
    else:
        raiz = pow(V, 0.5)
        i = 3
        while i <= raiz:
            if V % i == 0:
                return False
            i += 2
        return True

# programa principal
try:
    N = int(input('Digite um número inteiro: '))
    if Primo(N):
        print(f'{N} é primo')
    else:
        print(f'{N} não é primo')
except TypeError as te:
    print(f'Erro!! {te}')
except ValueError  as ve:
    print(f'Erro!! {ve}')