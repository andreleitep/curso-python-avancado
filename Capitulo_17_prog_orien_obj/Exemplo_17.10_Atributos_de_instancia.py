class Musica:
    def __init__(self, titulo, artista, album, ano, genero):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.ano = ano
        self.genero = genero
    def exibe(self):
        s = '{}\n    {}\n    {}\n    {}\n    {}'
        print(s.format(self.titulo, self.artista, self.album, self.ano, self.genero))

m1 = Musica('Time', 'Pink Floyd', 'The Dark Side of the Moon', 1973, 'Rock')
m2 = Musica('Óculos','Paralamas do Sucesso', 'O Passo do Lui', 1984, 'MPB')
m3 = Musica('Evidências', 'Chitãozinho e Xororó', 'Cowboy do Asfalto', 1990, 'Sertanejo')

print(m1.titulo)
print(m2.titulo)
print(m3.titulo)

m1.exibe()
m2.exibe()
m3.exibe()