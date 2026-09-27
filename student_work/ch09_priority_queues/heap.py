class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def swap(self, i, j):
        self.arreglo[i], self.arreglo[j] = self.arreglo[j], self.arreglo[i]

    def insert(self, valor):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1

        # Mientras sea menor que su padre, sube
        while i > 1 and self.arreglo[i] < self.arreglo[i // 2]:
            self.swap(i, i // 2)
            i = i // 2

    def remove_smallest(self):
        if len(self.arreglo) == 1:
            return None

        menor = self.arreglo[1]
        self.arreglo[1] = self.arreglo.pop()  # el último ocupa el lugar del primero

        i = 1
        n = len(self.arreglo)
        while 2 * i < n:
            hijo = 2 * i
            if hijo + 1 < n and self.arreglo[hijo + 1] < self.arreglo[hijo]:
                hijo = hijo + 1  # el hijo derecho es más pequeño

            if self.arreglo[i] <= self.arreglo[hijo]:
                break  # ya está en su lugar

            self.swap(i, hijo)
            i = hijo

        return menor

    def build_heap(self, lista):
        self.arreglo = [float('-inf')] + list(lista)
        n = len(self.arreglo)

        for i in range(n // 2, 0, -1):
            actual = i
            while 2 * actual < n:
                hijo = 2 * actual
                if hijo + 1 < n and self.arreglo[hijo + 1] < self.arreglo[hijo]:
                    hijo = hijo + 1

                if self.arreglo[actual] <= self.arreglo[hijo]:
                    break

                self.swap(actual, hijo)
                actual = hijo
