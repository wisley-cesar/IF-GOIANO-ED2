class No:
    def __init__(self, chave, cor, esquerda=None, direita=None, pai=None):
        self.chave = chave
        self.cor = cor
        self.esquerda = esquerda
        self.direita = direita
        self.pai = pai
        self.ocorrencias = 1


class ArvoreRubroNegra:
    def __init__(self):
        self.NIL = No(chave=None, cor='PRETO')
        self.raiz = self.NIL

    def inserir(self, chave):
        novo_no = No(chave, cor='VERMELHO')
        self._inserir(novo_no)
    def _inserir(self, z):
        y = self.NIL
        x = self.raiz

        while x != self.NIL:
            y = x
            if z.chave < x.chave:
                x = x.esquerda
            else:
                x = x.direita

        z.pai = y
        if y == self.NIL:
            self.raiz = z
        elif z.chave < y.chave:
            y.esquerda = z
        else:
            y.direita = z

        z.esquerda = self.NIL
        z.direita = self.NIL
        z.cor = 'VERMELHO'
        self._inserir_correcao(z)

    def _inserir_correcao(self, z):
        while z.pai.cor == 'VERMELHO':
            if z.pai == z.pai.pai.esquerda:
                y = z.pai.pai.direita
                if y.cor == 'VERMELHO':
                    z.pai.cor = 'PRETO'
                    y.cor = 'PRETO'
                    z.pai.pai.cor = 'VERMELHO'
                    z = z.pai.pai
                else:
                    if z == z.pai.direita:
                        z = z.pai
                        self.rotacao_esquerda(z)
                    z.pai.cor = 'PRETO'
                    z.pai.pai.cor = 'VERMELHO'
                    self.rotacao_direita(z.pai.pai)
            else:
                y = z.pai.pai.esquerda
                if y.cor == 'VERMELHO':
                    z.pai.cor = 'PRETO'
                    y.cor = 'PRETO'
                    z.pai.pai.cor = 'VERMELHO'
                    z = z.pai.pai
                else:
                    if z == z.pai.esquerda:
                        z = z.pai
                        self.rotacao_direita(z)
                    z.pai.cor = 'PRETO'
                    z.pai.pai.cor = 'VERMELHO'
                    self.rotacao_esquerda(z.pai.pai)

        self.raiz.cor = 'PRETO'

    def rotacao_esquerda(self, x):
        y = x.direita
        x.direita = y.esquerda

        if y.esquerda != self.NIL:
            y.esquerda.pai = x

        y.pai = x.pai

        if x.pai == self.NIL:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y

        y.esquerda = x
        x.pai = y

    def rotacao_direita(self, y):
        x = y.esquerda
        y.esquerda = x.direita

        if x.direita != self.NIL:
            x.direita.pai = y

        x.pai = y.pai

        if y.pai == self.NIL:
            self.raiz = x
        elif y == y.pai.direita:
            y.pai.direita = x
        else:
            y.pai.esquerda = x

        x.direita = y
        y.pai = x

    def caminhamento_em_ordem(self, no):
        if no != self.NIL:
            self.caminhamento_em_ordem(no.esquerda)
            print(f"Chave: {no.chave}, Cor: {no.cor}")
            self.caminhamento_em_ordem(no.direita)

    def contar_ocorrencias(self, raiz, numero):
        if raiz is None or raiz == self.NIL:
            return 0

        if numero == raiz.chave:
            return raiz.ocorrencias
        elif numero < raiz.chave:
            return self.contar_ocorrencias(raiz.esquerda, numero)
        else:
            return self.contar_ocorrencias(raiz.direita, numero)

    def contar_ocorrencias_chave(self, chave):
        return self.contar_ocorrencias(self.raiz, chave)