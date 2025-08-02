# Um pacote (package) é basicamente uma pasta com módulos
#   └─> O pacote pode conter um arquivo chamado __init__.py que executa todos os comandos que eu redigir
#       ao importar o pacote

import pacote.utils_bool
import pacote.utils_txt

print('-' * 20)
for s in dir():
    if '__' not in s:
        print(s)
print('-' * 20)

a = 2
print(pacote.utils_bool.texto)
r = pacote.utils_bool.primo(a)
print(f"{a} é primo? {r}")
r = pacote.utils_bool.paridade(a)
print(f"{a} é par? {r}")

print(pacote.utils_txt.texto)
pacote.utils_txt.primo(a)
pacote.utils_txt.paridade(a)

print("\nFim do programa")