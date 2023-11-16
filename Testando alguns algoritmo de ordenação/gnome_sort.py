def gnome_sort(arr):
    n = len(arr)
    index = 0

    while index < n:
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

    return arr

# Exemplo de uso:
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
resultado = gnome_sort(lista)
print(resultado)
