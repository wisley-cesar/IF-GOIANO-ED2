# Em CLIInterface.py, certifique-se de incluir todos os métodos necessários

from Arvore import ArvoreLivros
from Livro import Livro
from OrdenadorLivros import OrdenadorLivros

class CLIInterface:
    def __init__(self):
        self.arvore_livros = ArvoreLivros()

    def menu(self):
        while True:
            print("\n1. Cadastrar livro")
            print("2. Listar livros em ordem")
            print("3. Ordenar livros por título")
            print("4. Ordenar livros por gênero")
            print("5. Buscar por título")
            print("6. Buscar por autor")
            print("7. Buscar por gênero")
            print("8. Salvar dados")
            print("9. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.cadastrar_livro()
            elif choice == "2":
                self.listar_livros_em_ordem()
            elif choice == "3":
                self.ordenar_livros_por_titulo()
            elif choice == "4":
                self.ordenar_livros_por_genero()
            elif choice == "5":
                self.buscar_por_titulo()
            elif choice == "6":
                self.buscar_por_autor()
            elif choice == "7":
                self.buscar_por_genero()
            elif choice == "8":
                self.arvore_livros.salvar_dados()
            elif choice == "9":
                print("Saindo do programa. Até mais!")
                self.arvore_livros.salvar_dados()
                break
            else:
                print("Opção inválida. Tente novamente.")
    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        genero = input("Digite o gênero do livro: ")
        ano_publicacao = input("Digite o ano de publicação do livro: ")

        livro = Livro(titulo, autor, genero, int(ano_publicacao))
        self.arvore_livros.inserir(livro)
        print("Livro cadastrado com sucesso!")

    def listar_livros_em_ordem(self):
        print("\nÁrvore de Livros (em ordem):")
        self.arvore_livros.em_ordem()

    def ordenar_livros_por_titulo(self):
        livros = self.arvore_livros.obter_lista_livros()
        livros_ordenados_por_titulo = OrdenadorLivros.quicksort_por_titulo(livros)
        print("\nLivros ordenados por título:")
        for livro in livros_ordenados_por_titulo:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}")

    def ordenar_livros_por_genero(self):
        livros = self.arvore_livros.obter_lista_livros()
        livros_ordenados_por_genero = OrdenadorLivros.quicksort_por_genero(livros)
        print("\nLivros ordenados por gênero:")
        for livro in livros_ordenados_por_genero:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}")

    def buscar_por_titulo(self):
        titulo_a_buscar = input("Digite o título a ser buscado: ")
        livro_encontrado = self.arvore_livros.buscar_por_titulo(titulo_a_buscar)
        if livro_encontrado:
            print(f"\nLivro encontrado por título: {livro_encontrado.titulo}, Autor: {livro_encontrado.autor}")
        else:
            print("Livro não encontrado.")

    def buscar_por_autor(self):
        autor_a_buscar = input("Digite o autor a ser buscado: ")
        livro_encontrado = self.arvore_livros.buscar_por_autor(autor_a_buscar)
        if livro_encontrado:
            print(f"\nLivro encontrado por autor: {livro_encontrado.titulo}, Autor: {livro_encontrado.autor}")
        else:
            print("Livro não encontrado.")

    def buscar_por_genero(self):
        genero_a_buscar = input("Digite o gênero a ser buscado: ")
        livro_encontrado = self.arvore_livros.buscar_por_genero(genero_a_buscar)
        if livro_encontrado:
            print(f"\nLivro encontrado por gênero: {livro_encontrado.titulo}, Autor: {livro_encontrado.autor}")
        else:
            print("Livro não encontrado.")

