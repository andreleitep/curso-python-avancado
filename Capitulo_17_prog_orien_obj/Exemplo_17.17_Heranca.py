class Base:
    def exibe(self):
        print('Base')

class Herdeira(Base):
    def exibe2(self):
        print(' --- algo --- ')


obj = Herdeira()
obj.exibe()
obj.exibe2()