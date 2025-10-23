import sys
sys.path.append("I:\\Meu Drive\\ADS - Fatec\\Outros Cursos\\python-avancado\\Capitulo_17_prog_orien_obj\\cap17")
from cap17.modulo_exer_17_01_retangulo import Retangulo

retang = Retangulo(0, 0)
entrada = input("Escreva base e altura do retângulo (separado por espaço): ")
while entrada.lower() != "fim":
    ret = entrada.split()
    retang = Retangulo(float(ret[0]), float(ret[1]))
    retang.area()
    entrada = input("Escreva base e altura do retângulo (separado por espaço): ")