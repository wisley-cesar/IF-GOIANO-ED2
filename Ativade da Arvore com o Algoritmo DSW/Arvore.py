import random

class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def criar_arvore_aleatoria(tamanho):
    numeros = [random.randint(0, 100) for _ in range(tamanho)]
    raiz = None
    for num in numeros:
        raiz = inserir(raiz, num)
    return raiz

def imprimir_arvore(raiz):
    valores = []
    if raiz:
        imprimir_arvore_aux(raiz, valores)
    return valores

def imprimir_arvore_aux(raiz, valores):
    if raiz:
        imprimir_arvore_aux(raiz.esquerda, valores)
        valores.append(raiz.valor)
        imprimir_arvore_aux(raiz.direita, valores)

def inserir(raiz, valor):
    if raiz is None:
        return NoArvore(valor)
    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    else:
        raiz.direita = inserir(raiz.direita, valor)
    return raiz

def balancear_arvore(raiz):
    nos = []
    percorrer_in_order(raiz, nos)
    raiz, _ = realizar_rotacoes(raiz, len(nos))
    return raiz

def percorrer_in_order(raiz, nos):
    if raiz:
        percorrer_in_order(raiz.esquerda, nos)
        nos.append(raiz)
        percorrer_in_order(raiz.direita, nos)

def realizar_rotacoes(raiz, tamanho):
    if tamanho < 2:
        return raiz, None  # Correção: não há necessidade de retornar q quando tamanho < 2

    p = raiz
    q = p.esquerda
    for _ in range(tamanho):
        if q is not None:
            raiz = q
            p.esquerda = q.direita
            q.direita = p
            p = raiz
            q = p.esquerda
    return raiz, q

# Vamos criar a árvore inicial com 100 números aleatórios
arvore_inicial = criar_arvore_aleatoria(100)

# Vamos mostrar a árvore inicial
print(f'Árvore inicial: {imprimir_arvore(arvore_inicial)}\n')

# Adicionar 20 números à árvore
for _ in range(20):
    numero_adicional = random.randint(0, 100)
    arvore_inicial = inserir(arvore_inicial, numero_adicional)

# Vamos aplicar o algoritmo DSW na árvore após adicionar 20 números
arvore_inicial = balancear_arvore(arvore_inicial)

# Mostrar a árvore balanceada
print(f"Árvore balanceada após adicionar 20 números e aplicar o Algoritmo DSW: {imprimir_arvore(arvore_inicial)} ")
