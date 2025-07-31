# testar no idle

utilidades = 'este objeto é um string'
print(utilidades)
print(type(utilidades))
print(dir())
import sys
sys.path.append('H:\\Meu Drive\\ADS - FATEC\\Outros Cursos\\python-avancado\\Capitulo_16_modulos_e_pacotes')
import utilidades # à partir daqui o objeto 'utilidades' foi sobrescrito SEM AVISO
print(utilidades)