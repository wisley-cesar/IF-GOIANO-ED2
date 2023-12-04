import ast
import time

class No:
    def __init__(self, chave):
        self.chave = chave
        self.altura = 1
        self.esquerda = None
        self.direita = None

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def atualizar_altura(self, no):
        if no is not None:
            no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        self.atualizar_altura(y)
        self.atualizar_altura(x)

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        self.atualizar_altura(x)
        self.atualizar_altura(y)

        return y

    def inserir(self, raiz, chave):
        if raiz is None:
            return No(chave)

        if chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.inserir(raiz.direita, chave)
        else:
            return raiz  # Não são permitidas duplicatas

        self.atualizar_altura(raiz)

        balanceamento = self.balanceamento(raiz)

        # À esquerda
        if balanceamento > 1:
            if chave < raiz.esquerda.chave:
                return self.rotacao_direita(raiz)
            else:
                raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
                return self.rotacao_direita(raiz)

        # À direita
        if balanceamento < -1:
            if chave > raiz.direita.chave:
                return self.rotacao_esquerda(raiz)
            else:
                raiz.direita = self.rotacao_direita(raiz.direita)
                return self.rotacao_esquerda(raiz)

        return raiz

    def inserir_lista(self, chaves):
        for chave in chaves:
            self.raiz = self.inserir(self.raiz, chave)

    def percorrer_em_ordem(self, raiz):
        resultado = []
        if raiz:
            resultado += self.percorrer_em_ordem(raiz.esquerda)
            resultado.append(raiz.chave)
            resultado += self.percorrer_em_ordem(raiz.direita)
        return resultado



#