from cap17.m_exemplo_17_3 import Veiculo

def bar(whitch, n):
    match whitch:
        case 'ini':
            print('┌', '─' * (20 * n), '┐', sep='')
        case 'mid':
            print('├','─' * (20 * n), '┤', sep='')
        case 'fim':
            print('└', '─' * (20 * n), '┘', sep='')
        case _:
            print('─' * (21 * n))


DictV = {}
for i in open('veiculos.txt', 'r'):
    i = i.split(';')
    v = Veiculo(i[0], i[1], int(i[2]), int(i[3]))
    DictV[v.placa] = v

for a in DictV.values():
    a.exibe()

print()

for k in DictV.items():
    print(f'key: {k[0]} \n       └─> value: {k[1]}')

flag1 = 0
for j in DictV.values():
    if flag1 == 0:
        bar('ini', 2)
        flag1+=1
    else:
        bar('mid', 2)
    print(f'│ tipo da placa  {type(j.placa)} {' ' * 9} │')
    print(f'│ tipo do modelo {type(j.modelo)} {' ' * 9} │')
    print(f'│ tipo do ano    {type(j.ano)} {' ' * 9} │')
    print(f'│ tipo do km     {type(j.km)} {' ' * 9} │')
bar('fim', 2)

bar('', 2)

print('\nFim do Programa')