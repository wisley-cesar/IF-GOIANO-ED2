class NoAVL:
    def __init__(self, chave, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        self.altura = 1  # Altura padrão para um novo nó é 1
        self.ocorrencias = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def atualizar_altura(self, no):
        if no is not None:
            no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        # Realizar a rotação
        x.direita = y
        y.esquerda = T2

        # Atualizar alturas
        self.atualizar_altura(y)
        self.atualizar_altura(x)

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        # Realizar a rotação
        y.esquerda = x
        x.direita = T2

        # Atualizar alturas
        self.atualizar_altura(x)
        self.atualizar_altura(y)

        return y

    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def inserir(self, raiz, chave):
        if raiz is None:
            return NoAVL(chave)

        if chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.inserir(raiz.direita, chave)
        else:
            # Chaves iguais não são permitidas em uma árvore de busca binária
            raiz.ocorrencias += 1

        # Atualizar altura do nó atual
        self.atualizar_altura(raiz)

        # Obter o fator de balanceamento
        balanceamento = self.fator_balanceamento(raiz)

        # Casos de rotação
        # Rotação à direita simples (LL)
        if balanceamento > 1 and chave < raiz.esquerda.chave:
            return self.rotacao_direita(raiz)

        # Rotação à esquerda simples (RR)
        if balanceamento < -1 and chave > raiz.direita.chave:
            return self.rotacao_esquerda(raiz)

        # Rotação à esquerda-direita (LR)
        if balanceamento > 1 and chave > raiz.esquerda.chave:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Rotação à direita-esquerda (RL)
        if balanceamento < -1 and chave < raiz.direita.chave:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def inserir_chave(self, chave):
        self.raiz = self.inserir(self.raiz, chave)

    def contar_ocorrencias(self, raiz, numero):
        if raiz is None:
            return 0

        if numero == raiz.chave:
            return raiz.ocorrencias
        elif numero < raiz.chave:
            return self.contar_ocorrencias(raiz.esquerda, numero)
        else:
            return self.contar_ocorrencias(raiz.direita, numero)

    def contar_ocorrencias_chave(self, chave):
        return self.contar_ocorrencias(self.raiz, chave)

    def caminhamento_em_ordem(self, no):
        if no is not None:
            self.caminhamento_em_ordem(no.esquerda)
            print(f"Chave: {no.chave}, Altura: {no.altura}")
            self.caminhamento_em_ordem(no.direita)
