# Estrutura Union-Find com path compression e union by rank
class UnionFind:
    def __init__(self, vertices):
        self.representante = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        # Path compression: aponta direto para a raiz
        if self.representante[v] != v:
            self.representante[v] = self.find(self.representante[v])
        return self.representante[v]

    def union(self, a, b):
        raiz_a = self.find(a)
        raiz_b = self.find(b)
        if raiz_a == raiz_b:
            return  # Já no mesmo conjunto
        # Union by rank
        if self.rank[raiz_a] < self.rank[raiz_b]:
            raiz_a, raiz_b = raiz_b, raiz_a
        self.representante[raiz_b] = raiz_a
        if self.rank[raiz_a] == self.rank[raiz_b]:
            self.rank[raiz_a] += 1


# ✅ Função pedida no exercício
def temCiclo(origem, destino, uf):
    """
    Retorna True se adicionar a aresta (origem → destino) formaria um ciclo.
    Dica do exercício: se os representantes forem iguais → ciclo!
    """
    return uf.find(origem) == uf.find(destino)


# -------------------------------------------------------
# Teste com o "Exemplo Principal" típico de aula (Kruskal)
# Grafo com vértices A, B, C, D, E
# Arestas ordenadas por peso (como no algoritmo guloso)
# -------------------------------------------------------
vertices = ['A', 'B', 'C', 'D', 'E']
arestas = [
    (1, 'A', 'B'),
    (2, 'B', 'C'),
    (3, 'A', 'C'),  # ← esta fecha um ciclo A-B-C
    (4, 'C', 'D'),
    (5, 'D', 'E'),
    (6, 'B', 'E'),  # ← esta fecha um ciclo
]

uf = UnionFind(vertices)
mst = []

print("=== Processando arestas ===")
for peso, origem, destino in arestas:
    if temCiclo(origem, destino, uf):
        print(f"  ({origem}-{destino}, peso {peso}) → ❌ CICLO detectado, aresta ignorada")
    else:
        uf.union(origem, destino)
        mst.append((origem, destino, peso))
        print(f"  ({origem}-{destino}, peso {peso}) → ✅ Adicionada à MST")

print(f"\nÁrvore Geradora Mínima: {mst}")