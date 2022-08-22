class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # Como estamos trabalhando com herança, sendo a classe Programa a mãe, não é boa prática utilizarmos atributos privados,
    # portanto, utiliza-se apenas um underline("_") antes do atributo para que o Python ñ mude o nome daquele atributo e dificulte para chamarmos nas classes "filhas".

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # "super ()" é fazer dessa classe "filha" pegar referência através dos parâmetros da classe mãe (Programa)
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):  # O método "__getitem__" torna a classe interável, podendo utilizar laços ("for in")
        return self._programas[item]  # Repassando o item que estamos recebendo para uma lista de programas

    @property
    def listagem(self):
        return self._programas

    def __len__(self): # o método "__len__" possibilita a utilização de len dentro da classe Playlist
        return len(self._programas)


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
harry_potter = Filme("harry potter e o prisioneiro de askaban", 2012, 180)
one_piece = Serie("One Piece", 2000, 12)

one_piece.dar_likes()
one_piece.dar_likes()
one_piece.dar_likes()
one_piece.dar_likes()
one_piece.dar_likes()

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

harry_potter.dar_likes()

filmes_e_series = [vingadores, atlanta, harry_potter, one_piece]
playlist_fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

print(f'O tamanho da Playlist é de {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)
