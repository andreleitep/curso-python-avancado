# feito para testar no idle
"""
Quatro instâncias de namespace
1. __builtins__         --> vem junto com o python
2. instância global     --> relacionado a um programa em execução ou módulo
"""

# 1. __builtins__
print(dir(__builtins__))
# todos os comandos que usamos até então estão no namespace __builtins__ que faz parte do ambiente macro do python

"""
no idle:
sys.path.append('H:\\Meu Drive\\ADS - FATEC\\Outros Cursos\\python-avancado\\Capitulo_16_modulos_e_pacotes')
"""
#
import utilidades
print(dir(utilidades))
"""
resultado
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__spec__', 'meses', 'paridade', 'primo', 'texto', 'texto2']
  └─> instância global do módulo "utilidades"
"""
I = 10
F = 3.45
T = (1, 2, 3)
S = 'algo'
for a in dir():
    print(a)
"""
resultado
F
I
T
S
__annotations__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
utilidades (porque eu o importei)
  └─> instância (ou escopo) GLOBAL do próprio programa
"""
