class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Inserção
    def insert(self, paciente, dor):
        self.heap.append([dor, paciente])

        i = len(self.heap) - 1

        while i > 0 and self.heap[self.parent(i)][0] < self.heap[i][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    # Heapify para baixo
    def heapify(self, i):
        maior = i

        l = self.left(i)
        r = self.right(i)

        if l < len(self.heap) and self.heap[l][0] > self.heap[maior][0]:
            maior = l

        if r < len(self.heap) and self.heap[r][0] > self.heap[maior][0]:
            maior = r

        if maior != i:
            self.swap(i, maior)
            self.heapify(maior)

    # Atender paciente prioritário
    def extract_max(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify(0)

        return raiz

    # Aumentar prioridade
    def increase_key(self, nome, nova_dor):
        for i in range(len(self.heap)):
            if self.heap[i][1] == nome:

                if nova_dor <= self.heap[i][0]:
                    return

                self.heap[i][0] = nova_dor

                while i > 0 and self.heap[self.parent(i)][0] < self.heap[i][0]:
                    self.swap(i, self.parent(i))
                    i = self.parent(i)

                return

    # Diminuir prioridade
    def decrease_key(self, nome, nova_dor):
        for i in range(len(self.heap)):
            if self.heap[i][1] == nome:

                if nova_dor >= self.heap[i][0]:
                    return

                self.heap[i][0] = nova_dor

                self.heapify(i)

                return

    def mostrar(self):
        print(self.heap)

fila = MaxHeap()

fila.insert("João", 5)
fila.insert("Maria", 9)
fila.insert("Pedro", 3)
fila.insert("Ana", 7)

print("Fila inicial:")
fila.mostrar()