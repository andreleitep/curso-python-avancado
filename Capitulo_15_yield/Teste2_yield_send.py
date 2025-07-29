# fatorial
def fg_fatorial():
    num = 2
    mult = 1
    while True:
        while num > 0:
            res = yield (mult * num)
            num -= 1
        if res is not None:
            num = res

asd = fg_fatorial()
next(asd)
for i in range(6):
    print(asd.send(6))