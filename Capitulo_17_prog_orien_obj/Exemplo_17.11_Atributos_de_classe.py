class Contador:
    cont_instancias = 0
    def __init__(self):
        Contador.cont_instancias += 1

print(Contador.cont_instancias)

o1 = Contador()
print(o1.cont_instancias)
o2 = Contador()
print(o2.cont_instancias)
print(Contador.cont_instancias)

l = []
for i in range(5):
    l.append(f'objeto{i}')

d = {}
for i in l:
    d[i] = Contador()

for nome, obj in d.items():
    print(nome, obj.cont_instancias)

print(o1.cont_instancias)