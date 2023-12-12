import pickle

from NoArvore import NoArvore


class ArvoreLivros:
    def __init__(self):
        self.raiz = None

    def inserir(self, livro, no=None):
        if not no:
            no = self.raiz

        if not self.raiz:
            self.raiz = NoArvore(livro)
        else:
            if livro.titulo < no.livro.titulo:
                if not no.esquerda:
                    no.esquerda = NoArvore(livro)
                else:
                    self.inserir(livro, no.esquerda)
            elif livro.titulo > no.livro.titulo:
                if not no.direita:
                    no.direita = NoArvore(livro)
                else:
                    self.inserir(livro, no.direita)

    def em_ordem(self, no=None):
        if not no:
            no = self.raiz

        pilha = []
        while pilha or no:
            if no:
                pilha.append(no)
                no = no.esquerda
            else:
                no = pilha.pop()
                print(f"Título: {no.livro.titulo}, Autor: {no.livro.autor}, Ano: {no.livro.ano_publicacao}")
                no = no.direita

    def buscar_por_titulo(self, titulo, no=None):
        if not no:
            no = self.raiz

        while no:
            if titulo == no.livro.titulo:
                return no.livro
            elif titulo < no.livro.titulo:
                no = no.esquerda
            else:
                no = no.direita

        return None

    def buscar_por_autor(self, autor, no=None):
        if not no:
            no = self.raiz

        while no:
            if autor == no.livro.autor:
                return no.livro
            elif autor < no.livro.autor:
                no = no.esquerda
            else:
                no = no.direita

        return None

    def buscar_por_genero(self, genero, no=None):
        if not no:
            no = self.raiz

        while no:
            if genero == no.livro.genero:
                return no.livro
            elif genero < no.livro.genero:
                no = no.esquerda
            else:
                no = no.direita

        return None

    def salvar_dados(self, nome_arquivo='dados_livros.pkl'):
        try:
            with open(nome_arquivo, 'wb') as arquivo:
                pickle.dump(self.raiz, arquivo)
            print("Dados salvos com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def carregar_dados(self, nome_arquivo='dados_livros.pkl'):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                self.raiz = pickle.load(arquivo)
            print("Dados carregados com sucesso.")
        except FileNotFoundError:
            print("Arquivo não encontrado. Criando uma nova árvore.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
    def obter_lista_livros(self, no=None):
        if not no:
            no = self.raiz

        lista_livros = []
        pilha = []

        while pilha or no:
            if no:
                pilha.append(no)
                no = no.esquerda
            else:
                no = pilha.pop()
                lista_livros.append(no.livro)
                no = no.direita

        return lista_livros