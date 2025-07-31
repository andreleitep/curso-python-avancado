# testar no idle

import sys
sys.path.append('H:\\Meu Drive\\ADS - FATEC\\Outros Cursos\\python-avancado\\Capitulo_16_modulos_e_pacotes')
import utilidades
print('\nescopo global =', dir())
print('\nescopo local do módulo "utilidades" =', dir(utilidades))
# print(texto)
#   └─> não vai funcionar porque no escopo global do programa não há o elemento texto
#       Apenas no escopo local do módulo utilidades temos esse elemento.
#       Para acessá-lo, é necessário fazer a notação com ponto!
print()
print(utilidades.texto)
