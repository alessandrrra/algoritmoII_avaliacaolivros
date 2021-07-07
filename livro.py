'''
Implementar uma pilha de objetos Livro.
O objeto Livro também deve possuir os atributos id, título e autor.
O atributo autor será utilizado para armazenar um objeto do tipo Autor.
A classe Autor deve possuir o atributo fracamente privado id e o atributo público nome.
O sistema deverá possuir métodos para inserir e para retirar livros da pilha.
'''

class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self._size = 0

    def imprimir(self):
        print("Identificação do livro:", self.id, "Título:", self.titulo, "Autor:", self.autor.nome)