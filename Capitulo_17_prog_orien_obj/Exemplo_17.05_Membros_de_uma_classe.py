# Testar no Idle

# visibilidades: Público, Protegido, Privado

lista = [2, 4, 6, 8]
i = 1
for j in dir(lista):
    print(j, end=' ')
    if i % 10 == 0:
        print()
    i+=1