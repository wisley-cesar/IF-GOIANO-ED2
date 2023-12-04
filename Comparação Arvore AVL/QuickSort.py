class QuickSort:
    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            menores = [x for x in arr[1:] if x <= pivot]
            maiores = [x for x in arr[1:] if x > pivot]
            return self.sort(menores) + [pivot] + self.sort(maiores)
