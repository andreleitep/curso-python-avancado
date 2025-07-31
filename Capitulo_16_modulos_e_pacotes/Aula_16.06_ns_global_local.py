def funcao1():
    print('   ... inicio da funcao1')
    if criterio == 'alterar':
        valor = 999
    print(f'   ... valor dentro da funcao1 = {valor}')

def funcao2():
    print('   ... inicio da funcao2')
    global valor # chama a variável de fora da função
    if criterio == 'alterar':
        valor = 999
    print(f'   ... valor dentro da funcao2 = {valor}')


criterio = 'alterar'
valor = 10
print(f'programa principal valor = {valor} (antes funcao1)')
funcao1()
print(f'programa principal valor = {valor} (após a funcao1)')

print('-----------------------------------------------------')

print(f'programa principal valor = {valor} (antes funcao2)')
funcao2()
print(f'programa principal valor = {valor} (após a funcao2)')