from tkinter.font import names

from cap17.m_exemplo_17_3 import Veiculo

def bar(whitch, n):
    match whitch:
        case 'ini':
            print('┌', '─' * (20 * n), '┐', sep='')
        case 'mid':
            print('├','─' * (20 * n), '┤', sep='')
        case 'end':
            print('└', '─' * (20 * n), '┘', sep='')
        case _:
            print('─' * (21 * n))


DictV = {}
for i in open('veiculos.txt', 'r'):
    i = i.split(';')
    v = Veiculo(i[0], i[1], int(i[2]), int(i[3]))
    DictV[v.placa] = v

print()

flag2 = 0
for a in DictV.values():
    if flag2 == 0:
        bar('ini', 3)
        flag2+=1
    else:
        bar('mid', 3)
    a.exibe()
bar('end', 3)

print()

for k in DictV.items(): # retorna uma tupla (key, value), por isso dá para indicar com [#]
    print(f'┌──────────────┐')
    print(f'│ key: {k[0]} │\n'
          f'├──────────────┴────────────────────────────────────────────────────────────────┐\n'
          f'│        └─> value: {k[1]} │\n'
          f'└───────────────────────────────────────────────────────────────────────────────┘')

print()

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
bar('end', 2)

print()

namespace_list = []
for e in dir():
    if '__' in e:
        pass
    else:
        namespace_list.append(e)

print('┌─────────────────┐')
print('│ Lista do dir(): │\n'
      '├─────────────────┴────────────────────────────────────────────────────────────────────┐\n'
      '│         └─>', ', '.join(namespace_list), ' │\n'
      '└──────────────────────────────────────────────────────────────────────────────────────┘')

print('\nFim do Programa')