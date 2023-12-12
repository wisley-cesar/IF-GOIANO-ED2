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
                print(f"Título: {no.livro.titulo}, Autor: {no.livro.autor}, Ano: {no.livro.ano_publicacao}, Gênero: {no.livro.genero}")
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

    def buscar_por_autor(self, autor):
        return self._buscar_por_autor(self.raiz, autor)

    def _buscar_por_autor(self, no, autor):
        if not no:
            return None

        if autor == no.livro.autor:
            return no.livro
        elif autor < no.livro.autor:
            return self._buscar_por_autor(no.esquerda, autor)
        else:
            return self._buscar_por_autor(no.direita, autor)

    def buscar_por_genero(self, genero):
        return self._buscar_por_genero(self.raiz, genero)

    def _buscar_por_genero(self, no, genero):
        if not no:
            return None

        if genero == no.livro.genero:
            return no.livro
        elif genero < no.livro.genero:
            return self._buscar_por_genero(no.esquerda, genero)
        else:
            return self._buscar_por_genero(no.direita, genero)

    def salvar_dados(self, nome_arquivo='dados_livros.pkl'):
        lista_livros = self.obter_lista_livros()
        try:
            with open(nome_arquivo, 'wb') as arquivo:
                for livro in lista_livros:
                    pickle.dump(livro, arquivo)
            print("Dados salvos com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def carregar_dados(self, nome_arquivo='dados_livros.pkl'):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                while True:
                    try:
                        livro = pickle.load(arquivo)
                        print(f"Livro carregado: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Ano: {livro.ano_publicacao}")
                        self.inserir(livro)
                    except EOFError:
                        break
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

    def remover_por_titulo(self, titulo):
        self.raiz = self._remover_por_titulo(self.raiz, titulo)

    def _remover_por_titulo(self, no, titulo):
        if not no:
            return None

        if titulo < no.livro.titulo:
            no.esquerda = self._remover_por_titulo(no.esquerda, titulo)
        elif titulo > no.livro.titulo:
            no.direita = self._remover_por_titulo(no.direita, titulo)
        else:
            # Nó a ser removido encontrado
            if not no.esquerda:
                return no.direita
            elif not no.direita:
                return no.esquerda

            # Nó tem dois filhos, encontrar sucessor (menor valor na subárvore direita)
            sucessor = self._min_valor_no(no.direita)
            no.livro = sucessor.livro
            no.direita = self._remover_por_titulo(no.direita, sucessor.livro.titulo)

        return no

    def _min_valor_no(self, no):
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual
