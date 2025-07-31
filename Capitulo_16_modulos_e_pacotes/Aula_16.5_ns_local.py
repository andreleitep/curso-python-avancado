# o escopo local é o que abrange uma função
def soma(a, b):
    print('Parte 3 -Namespace do local - função soma')
    for s in dir():
        print(s)
    return a + b

def diferenca(x, y):
    print('Parte 3 -Namespace do local - função soma')
    for s in dir():
        print(s)
    return x - y

print('Parte 1 -Namespace do interpretador Python built-in')
print(dir(__builtins__))
print('Parte 2 - Namespace global do programa')
v1 = 8
v2 = -36
for a in dir():
    if '__' not in a:
        print(a)

rs = soma(v1, v2)
rd = diferenca(v1, v2)

print(f'\n{v1} + {v2} = {rs}')
print(f'{v1} - {v2} = {rd}')