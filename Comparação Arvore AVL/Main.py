import ast
import time

from ArvoreAVL import ArvoreAVL
from QuickSort import QuickSort


class Main:
    @staticmethod
    def main():
        # Carregar números do arquivo
        with open("dados100_mil.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        numeros = []
        for linha in linhas:
            numeros.extend(ast.literal_eval(linha))

        # Medir o tempo para a Árvore AVL
        inicio_avl = time.time()
        arvore_avl = ArvoreAVL()
        arvore_avl.inserir_lista(numeros.copy())
        resultado_avl = arvore_avl.percorrer_em_ordem(arvore_avl.raiz)
        fim_avl = time.time()

        # Exibir resultados da Árvore AVL
        print("Árvore AVL construída e impressa em ordem em {:.6f} segundos.".format(fim_avl - inicio_avl))
        print("Primeiros 10 elementos em ordem:")
        print(resultado_avl[:])

        # Medir o tempo para Quick Sort
        inicio_quick_sort = time.time()
        quick_sort_instance = QuickSort()
        numeros_ordenados_quick_sort = quick_sort_instance.sort(numeros.copy())
        fim_quick_sort = time.time()

        # Exibir resultados do Quick Sort
        print("\nQuick Sort concluído em {:.6f} segundos.".format(fim_quick_sort - inicio_quick_sort))
        print("Primeiros 10 elementos ordenados:")
        print(numeros_ordenados_quick_sort[:])

        print("\nÁrvore AVL construída e impressa em ordem em {:.6f} segundos.".format(fim_avl - inicio_avl))
        print("\nQuick Sort concluído em {:.6f} segundos.".format(fim_quick_sort - inicio_quick_sort))


if __name__ == "__main__":
    Main.main()
