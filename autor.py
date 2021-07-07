from livro import Livro

class Autor:
    def __init__(self, idautor, nome):
        self._idautor = idautor
        self.nome = nome

    def imprimir(self):
        print("Identificação do autor:", self._idautor, "Nome:", self.nome)