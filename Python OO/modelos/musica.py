
""""
No Python, a criação de classes é uma parte essencial da programação orientada a objetos. 
Abaixo, temos um exemplo de uma classe chamada Musica que representa informações sobre uma música, como nome, artista e duração:

"""
class Musica:
    musicas = []  # Lista compartilhada entre todas as instâncias da classe

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)  # Adiciona a instância atual à lista

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

    @staticmethod
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')


# Criação dos objetos
musica1 = Musica('Sweet Child O\' Mine', 'Guns N\' Roses', '5:56')
musica2 = Musica('Bohemian Rhapsody', 'Queen', '5:54')
musica3 = Musica('Enter Sandman', 'Metallica', '5:32')

# Chamada do método listar_musicas para exibir as músicas
Musica.listar_musicas()
