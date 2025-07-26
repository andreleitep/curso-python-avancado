def Paridade(pValor):
    '''
    if type(pValor) != int:
        raise Exception('A função paridade deve receber um int')
    '''
    if not isinstance(pValor, int):
        raise Exception('A função paridade deve receber um int')
    if pValor % 2 == 0:
        return 'PAR'
    else:
        return 'IMPAR'

n = int(input('Digite algo: '))
r = Paridade(n)
print(f'{n} é {r}')