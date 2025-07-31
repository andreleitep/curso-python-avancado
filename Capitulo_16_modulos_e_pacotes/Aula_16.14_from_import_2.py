import sys
sys.path.append('H:\\Meu Drive\\ADS - FATEC\\Outros Cursos\\python-avancado\\Capitulo_16_modulos_e_pacotes')
texto = '... string pré-existente ...'
paridade = 90
print(dir())
print(texto)
print(paridade)

from utilidades import texto, paridade, meses
print(dir())
print('-------------------------')
print(texto)
print(paridade)