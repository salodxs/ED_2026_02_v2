import matplotlib.pyplot as plt

class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]
    def bajar(self, i):
        A = self.arreglo
        while 2 * i < len(A):
            h = 2 * i
            if h + 1 < len(A) and A[h + 1] < A[h]:
                h += 1
            if A[h] >= A[i]:
                break
            A[i], A[h] = A[h], A[i]
            i = h

    def insert(self, valor, imagen=False):
        A = self.arreglo
        A.append(valor)
        i = len(A) - 1
        while A[i // 2] > A[i]:          # el -inf de A[0] lo detiene solo
            A[i], A[i // 2] = A[i // 2], A[i]
            i = i // 2
        if imagen: self.dibujar()

    def remove_smallest(self, imagen=False):
        A = self.arreglo
        menor = A[1]
        A[1] = A[-1]
        A.pop()
        self.bajar(1)
        if imagen: self.dibujar()
        return menor

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        for i in range(len(lista) // 2, 0, -1):
            self.bajar(i)
        if imagen: self.dibujar()

    def dibujar(self):
        A = self.arreglo
        pos = lambda i: ((i - 2**(i.bit_length()-1) + 0.5) / 2**(i.bit_length()-1), -i.bit_length())
        plt.figure(figsize=(10, 5))
        for i in range(1, len(A)):
            x, y = pos(i)
            if i > 1:                     # línea hacia el padre
                px, py = pos(i // 2)
                plt.plot([x, px], [y, py], 'k-')
            plt.text(x, y, A[i], ha='center', va='center',
                     bbox=dict(boxstyle='circle', fc='lightblue'))
        plt.axis('off')
        plt.show()
