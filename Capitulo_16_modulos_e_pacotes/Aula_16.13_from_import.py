# testar no idle

import sys
sys.path.append('H:\\Meu Drive\\ADS - FATEC\\Outros Cursos\\python-avancado\\Capitulo_16_modulos_e_pacotes')
print(dir())
from utilidades import paridade # desta maneira posso utilizar diretamente o elemento paridade sem precisar de notação com ponto
print(dir())
print(paridade(9))
from random import randint
print(randint(10, 20))