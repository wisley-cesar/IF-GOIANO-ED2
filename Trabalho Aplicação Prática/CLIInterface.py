from Arvore import ArvoreLivros
from Livro import Livro
from OrdenadorLivros import OrdenadorLivros

class CLIInterface:
    def __init__(self):
        self.arvore_livros = ArvoreLivros()
        self.arvore_livros.carregar_dados()  # Carregar dados ao iniciar o programa

    def menu(self):
        while True:
            print("\n1. Cadastrar livro")
            print("2. Listar livros em ordem")
            print("3. Ordenar livros por título")
            print("4. Ordenar livros por gênero")
            print("5. Buscar por título")
            print("6. Buscar por autor")
            print("7. Buscar por gênero")
            print("8. Remover livro por título")
            print("9. Salvar dados")
            print("10. Sair")

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
                self.remover_livro_por_titulo()
            elif choice == "9":
                self.arvore_livros.salvar_dados()
            elif choice == "10":
                print("Saindo do programa. Até mais!")
                self.arvore_livros.salvar_dados()
                break
            else:
                print("Opção inválida. Tente novamente.")

    def remover_livro_por_titulo(self):
        titulo_a_remover = input("Digite o título do livro a ser removido: ").strip()
        self.arvore_livros.remover_por_titulo(titulo_a_remover)
        print("Livro removido com sucesso.")

    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ").strip()
        autor = input("Digite o autor do livro: ").strip()
        genero = input("Digite o gênero do livro: ").strip()
        ano_publicacao = input("Digite o ano de publicação do livro: ").strip()

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
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}, Gênero: {livro.genero}")

    def ordenar_livros_por_genero(self):
        livros = self.arvore_livros.obter_lista_livros()
        livros_ordenados_por_genero = OrdenadorLivros.quicksort_por_genero(livros)
        print("\nLivros ordenados por gênero:")
        for livro in livros_ordenados_por_genero:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}, Gênero: {livro.genero}")

    def buscar_por_titulo(self):
        titulo_a_buscar = input("Digite o título a ser buscado: ").strip()
        livro_encontrado = self.arvore_livros.buscar_por_titulo(titulo_a_buscar)
        if livro_encontrado:
            print(f"\nLivro encontrado por título: {livro_encontrado.titulo}, Autor: {livro_encontrado.autor}, Gênero: {livro_encontrado.genero}")
        else:
            print("Livro não encontrado.")

    def buscar_por_autor(self):
        autor_a_buscar = input("Digite o autor a ser buscado: ").strip()
        livro_encontrado = self.arvore_livros.buscar_por_autor(autor_a_buscar)
        if livro_encontrado:
            print(f"\nLivro encontrado por autor: {livro_encontrado.titulo}, Autor: {livro_encontrado.autor}, Gênero: {livro_encontrado.genero}")
        else:
            print("Livro não encontrado.")

    def buscar_por_genero(self):
        genero_a_buscar = input("Digite o gênero a ser buscado: ").strip()
        livro_encontrado = self.arvore_livros.buscar_por_genero(genero_a_buscar)
        if livro_encontrado:
            print(f"\nLivro encontrado por gênero: {livro_encontrado.titulo}, Autor: {livro_encontrado.autor}, Gênero: {livro_encontrado.genero}")
        else:
            print("Livro não encontrado.")
