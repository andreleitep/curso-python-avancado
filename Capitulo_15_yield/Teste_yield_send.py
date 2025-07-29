def fg_tabuada():
    mult = 2
    num = 0
    while True:
        outro = (yield num * mult)
        num += 1
        if outro is not None:
            num = 1
            mult = outro

tabuada = fg_tabuada()
next(tabuada)

n = int(input("Que número? "))
ret = tabuada.send(n)
print(ret)
for i in range(9):
    print(next(tabuada))