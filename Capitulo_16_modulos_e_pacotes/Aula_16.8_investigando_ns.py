# para testar no idle

print(dir())
a = 236
b = 17.3
txt = 'algum texto'
r = 0
print(dir())
del(r)
print(dir())
import sys
# no idle não precisa da barra dupla
sys.path.append('H:\\Meu Drive\\ADS - FATEC\\Outros Cursos\\python-avancado\\Capitulo_16_modulos_e_pacotes')
import utilidades
print(dir())
print(dir(utilidades))

for s in dir(utilidades):
    if '__' not in s:
        print(s)

for s in dir(sys):
    print(s)
