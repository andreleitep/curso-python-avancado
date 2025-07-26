import sys
import cProfile

quadrados_lc = [num**2 for num in range(1, 10001)] # list comprehension
type(quadrados_lc) # list (armazena os valores na memória, ocupando espaço)
print(quadrados_lc)

quadrados_eg = (num**2 for num in range(1, 10001)) # expressão geradora
type(quadrados_eg) # generator (a diferença é que o generator só poderá ser utilizado uma vez)
print(quadrados_eg) # não armazena os valores na memória, os geraquando é chamada

for valor in quadrados_lc:
    print(valor, end=' ')

print('\nquadrados_lc =', sys.getsizeof(quadrados_lc))
print('quadrados_eg =', sys.getsizeof(quadrados_eg))

# for valor in quadrados_eg:
#     print(valor, end=' ')

print(cProfile.run('sum([num**2 for num in range(1, 1000001)])'))
print(cProfile.run('sum((num**2 for num in range(1, 1000001)))'))

'''
Se eu tiver como gargalo a memória do computador, é melhor usar expressão geradora
Se, do contrário, eu tiver o tempo de processamento como gargalo, é melhor usar list comprehention
'''