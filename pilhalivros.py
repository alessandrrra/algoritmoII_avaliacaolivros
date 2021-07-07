from livro import Livro

class Livros:
    def __init__(self):
        self.top = None
        self._size = 0

    def inserir(self, elem):
        #inserir livro
        livro = elem
        livro.next = self.top
        self.top = livro
        self._size = self._size + 1

    def tirar(self):
        #remove um livro
        if self._size > 0:
            livro = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return livro
        raise IndexError("A pilha está vazia.")

    def imprimir(self):
        print(Livros)