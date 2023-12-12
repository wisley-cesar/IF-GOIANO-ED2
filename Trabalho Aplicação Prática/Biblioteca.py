class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def quicksort(self, lista, chave):
        if len(lista) <= 1:
            return lista
        else:
            pivot = lista[0]
            menores = [livro for livro in lista[1:] if getattr(livro, chave) < getattr(pivot, chave)]
            maiores = [livro for livro in lista[1:] if getattr(livro, chave) >= getattr(pivot, chave)]
            return self.quicksort(menores, chave) + [pivot] + self.quicksort(maiores, chave)

    def ordenar_por_chave(self, chave):
        self.livros = self.quicksort(self.livros, chave)
