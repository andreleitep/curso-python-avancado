# testar no idle

import sys
sys.path.append('H:\\Meu Drive\\ADS - FATEC\\Outros Cursos\\python-avancado\\Capitulo_16_modulos_e_pacotes')
import utilidades

print('\nimport utilidades\n')

for s in dir():
    print(s)

print('\ndir(utilidades)\n')

for s in dir(utilidades):
    print(s)

print('\nfrom utilidades import *\n')

from utilidades import *
# Quando eu utilizo o coringa ('*') o python não importa os elementos com duplo underline ('__')
for s in dir():
    print(s)

print('\n', texto)