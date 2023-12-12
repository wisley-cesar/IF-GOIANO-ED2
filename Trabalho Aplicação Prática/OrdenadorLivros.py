class OrdenadorLivros:
    @staticmethod
    def quicksort_por_titulo(livros):
        if len(livros) <= 1:
            return livros
        else:
            pivot = livros[0]
            menores = [livro for livro in livros[1:] if livro.titulo < pivot.titulo]
            maiores = [livro for livro in livros[1:] if livro.titulo >= pivot.titulo]
            return OrdenadorLivros.quicksort_por_titulo(menores) + [pivot] + OrdenadorLivros.quicksort_por_titulo(maiores)

    @staticmethod
    def quicksort_por_genero(livros):
        if len(livros) <= 1:
            return livros
        else:
            pivot = livros[0]
            menores = [livro for livro in livros[1:] if livro.genero < pivot.genero]
            maiores = [livro for livro in livros[1:] if livro.genero >= pivot.genero]
            return OrdenadorLivros.quicksort_por_genero(menores) + [pivot] + OrdenadorLivros.quicksort_por_genero(maiores)
