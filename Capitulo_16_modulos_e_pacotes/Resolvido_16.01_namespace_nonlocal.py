def valor_venda(codigo, val_custo):

    def altera_margem(): # não funciona porque o objeto margem é local a esta função, não à função container
        if codigo[0] == '8': # └─> para resolver isso, precisamos declarar dentro desta função aninhada o objeto
            margem = 0.12 #        margem como nonlocal ("nonlocal margem")
        if codigo[0] == '9':
            margem = 0.10
    margem = 0.16
    altera_margem()
    val_venda = val_custo * (1 + margem)
    return val_venda

def valor_venda2(codigo, val_custo):

    def altera_margem():
        nonlocal margem
        if codigo[0] == '8':
            margem = 0.12
        if codigo[0] == '9':
            margem = 0.10
    margem = 0.16
    altera_margem()
    val_venda = val_custo * (1 + margem)
    return val_venda

PcCusto = 100
CodProd = '1280'
PcVenda = valor_venda(CodProd, PcCusto)
print(f'Produto {CodProd}: compra = {PcCusto:.2f} e venda = {PcVenda:.2f}')

PcCusto = 100
CodProd = '8280'
PcVenda = valor_venda(CodProd, PcCusto)
print(f'Produto {CodProd}: compra = {PcCusto:.2f} e venda = {PcVenda:.2f}')

PcCusto = 100
CodProd = '9280'
PcVenda = valor_venda(CodProd, PcCusto)
print(f'Produto {CodProd}: compra = {PcCusto:.2f} e venda = {PcVenda:.2f}')

print('\n','-' * 44,'\n')

PcCusto = 100
CodProd = '1280'
PcVenda = valor_venda2(CodProd, PcCusto)
print(f'Produto {CodProd}: compra = {PcCusto:.2f} e venda = {PcVenda:.2f}')

PcCusto = 100
CodProd = '8280'
PcVenda = valor_venda2(CodProd, PcCusto)
print(f'Produto {CodProd}: compra = {PcCusto:.2f} e venda = {PcVenda:.2f}')

PcCusto = 100
CodProd = '9280'
PcVenda = valor_venda2(CodProd, PcCusto)
print(f'Produto {CodProd}: compra = {PcCusto:.2f} e venda = {PcVenda:.2f}')