from livro import Livro
from autor import Autor
from pilhalivros import Livros

divisor = "-----"

a1 = Autor(1, "Alessandra")
a1.imprimir()

print(divisor)

l1 = Livro(1, "A viagem do dragão", a1)
l1.imprimir()

print(divisor)

livros = Livros()
livros.imprimir()

print(divisor)

'''
livros.inserir(l1)

print(divisor)

livros.tirar(l1)
'''