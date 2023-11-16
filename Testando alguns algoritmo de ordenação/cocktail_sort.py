def cocktail_sort(arr):
    n = len(arr)
    trocado = True
    inicio = 0
    fim = n - 1

    while (trocado == True):
        # Redefine o sinalizador de troca em cada passo
        trocado = False

        # Move o maior elemento para a direita
        for i in range(inicio, fim):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                trocado = True

        if (trocado == False):
            break

        # Redefine o sinalizador de troca para a próxima iteração
        trocado = False

        # Move o menor elemento para a esquerda
        fim = fim - 1

        for i in range(fim - 1, inicio - 1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                trocado = True

        inicio = inicio + 1

# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
cocktail_sort(arr)
print("Array ordenado:")
print(arr)
