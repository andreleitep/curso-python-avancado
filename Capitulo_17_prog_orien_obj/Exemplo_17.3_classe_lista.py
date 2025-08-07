from cap17.m_exemplo_17_3 import Veiculo

LstV = []
for s in open('veiculos.txt', 'r'):
    s = s.split(';')
    v = Veiculo(s[0], s[1], int(s[2]), int(s[3]))
    LstV.append(v)

for v in LstV:
    v.exibe()

print('\nFim do programa.')