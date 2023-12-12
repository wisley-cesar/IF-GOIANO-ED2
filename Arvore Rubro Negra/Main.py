import ast
import random
import time

from ArvoreAVL import ArvoreAVL
from Arvore_Rubro_Negra import ArvoreRubroNegra


def main():
    # Carregar números do arquivo
    with open("dados100_mil.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    numeros = []
    for linha in linhas:
        numeros.extend(ast.literal_eval(linha))

    # Exemplo de uso para medir o tempo de uma árvore AVL:
    arvore_avl = ArvoreAVL()
    inicio_avl = time.time()
    for chave in numeros:
        arvore_avl.inserir_chave(chave)
    fim_avl = time.time()

    tempo_avl = fim_avl - inicio_avl
    print(f"Tempo para preencher a árvore AVL: {tempo_avl} segundos")

    # Exemplo de uso para medir o tempo de uma árvore rubro-negra:
    arvore_rubro_negra = ArvoreRubroNegra()
    inicio_rubro_negra = time.time()
    for chave in numeros:
        arvore_rubro_negra.inserir(chave)
    fim_rubro_negra = time.time()

    tempo_rubro_negra = fim_rubro_negra - inicio_rubro_negra
    print(f"Tempo para preencher a árvore Rubro-Negra: {tempo_rubro_negra} segundos")

    # Sortear aleatoriamente outros 50.000 números entre -9999 e 9999
    populacao = range(-9999, 10000)
    numeros_sorteados = random.sample(populacao, min(50000, len(populacao)))

    # Operações após a inserção
    for numero in numeros_sorteados:
        if numero % 3 == 0:
            # Inserir número na árvore
            arvore_avl.inserir_chave(numero)
            arvore_rubro_negra.inserir(numero)
        elif numero % 5 == 0:
            # Remover número da árvore
            # Implemente o método de remoção na árvore AVL e Rubro-Negra
            pass
        else:
            # Contar quantas vezes o número aparece na árvore
            contador_avl = arvore_avl.contar_ocorrencias_chave(numero)
            contador_rubro_negra = arvore_rubro_negra.contar_ocorrencias(arvore_rubro_negra.raiz, numero)

            print(f"O número {numero} aparece {contador_avl} vezes na árvore AVL.")
            print(f"O número {numero} aparece {contador_rubro_negra} vezes na árvore Rubro-Negra.")


if __name__ == "__main__":
    main()
