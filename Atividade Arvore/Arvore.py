import random  # Importa a biblioteca random para gerar números aleatórios.

class NoArvore:
    def __init__(self, valor):
        self.valor = valor  # Inicializa um nó da árvore com um valor.
        self.esquerda = None  # Inicializa o filho esquerdo como nulo.
        self.direita = None  # Inicializa o filho direito como nulo.

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None  # Inicializa a árvore com uma raiz nula.

    def inserir(self, valor):
        if not self.raiz:  # Se a árvore estiver vazia, insere o valor na raiz.
            self.raiz = NoArvore(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)  # Caso contrário, chama uma função recursiva para inserir o valor.

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:  # Compara o valor a ser inserido com o valor do nó atual.
            if no.esquerda is None:  # Se o filho esquerdo estiver vazio, insere o valor lá.
                no.esquerda = NoArvore(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)  # Caso contrário, chama a função recursiva para o filho esquerdo.
        else:
            if no.direita is None:  # Se o filho direito estiver vazio, insere o valor lá.
                no.direita = NoArvore(valor)
            else:
                self._inserir_recursivo(no.direita, valor)  # Caso contrário, chama a função recursiva para o filho direito.

    def preordem(self, no):
        if no:
            print(no.valor, end=" ")  # Imprime o valor do nó atual.
            self.preordem(no.esquerda)  # Chama a função recursiva para o filho esquerdo.
            self.preordem(no.direita)  # Chama a função recursiva para o filho direito.

    def emordem(self, no):
        if no:
            self.emordem(no.esquerda)  # Chama a função recursiva para o filho esquerdo.
            print(no.valor, end=" ")  # Imprime o valor do nó atual.
            self.emordem(no.direita)  # Chama a função recursiva para o filho direito.

    def posordem(self, no):
        if no:
            self.posordem(no.esquerda)  # Chama a função recursiva para o filho esquerdo.
            self.posordem(no.direita)  # Chama a função recursiva para o filho direito.
            print(no.valor, end=" ")  # Imprime o valor do nó atual.

    def nivel(self):
        if not self.raiz:
            return

        fila = [self.raiz]  # Inicializa uma fila com a raiz da árvore.
        while fila:
            no = fila.pop(0)  # Remove o primeiro nó da fila.
            print(no.valor, end=" ")  # Imprime o valor do nó atual.
            if no.esquerda:
                fila.append(no.esquerda)  # Adiciona o filho esquerdo à fila, se existir.
            if no.direita:
                fila.append(no.direita)  # Adiciona o filho direito à fila, se existir.

def principal():
    random.seed(42)  # Define uma semente para a geração de números aleatórios, garantindo a reprodutibilidade dos resultados.
    numeros = random.sample(range(101), 20)  # Gera 20 números aleatórios exclusivos no intervalo de 0 a 100.

    arvore = ArvoreBinaria()  # Cria uma instância de uma árvore binária.
    for numero in numeros:
        arvore.inserir(numero)  # Insere os números gerados na árvore.

    # Imprime os resultados da árvore original.
    print("Árvore original:")
    print("Pré-ordem:", end=" ")
    arvore.preordem(arvore.raiz)
    print("\nEm ordem:", end=" ")
    arvore.emordem(arvore.raiz)
    print("\nPós-ordem:", end=" ")
    arvore.posordem(arvore.raiz)
    print("\nEm nível:", end=" ")
    arvore.nivel()

    # Remove 5 elementos da árvore e imprime novamente.
    print("\n\nRemovendo 5 elementos da árvore:")
    for i in range(5):
        no_a_remover = random.choice(numeros)  # Escolhe um número aleatório para remover da árvore.
        numeros.remove(no_a_remover)  # Remove o número da lista de números.
        arvore = ArvoreBinaria()  # Cria uma nova árvore.
        for numero in numeros:
            arvore.inserir(numero)  # Insere os números atualizados na nova árvore.

        # Imprime os resultados da árvore após a remoção.
        print(f"\nÁrvore após a remoção do elemento {no_a_remover}:")
        print("Pré-ordem:", end=" ")
        arvore.preordem(arvore.raiz)
        print("\nEm ordem:", end=" ")
        arvore.emordem(arvore.raiz)
        print("\nPós-ordem:", end=" ")
        arvore.posordem(arvore.raiz)
        print("\nEm nível:", end=" ")
        arvore.nivel()

if __name__ == "__main__":
    principal()  # Chama a função principal quando o scri2pt é executado.

