from collections import defaultdict

class Graph:
    def __init__(self, adj):
        self.adj = adj
        self.V = len(adj)  # Número de vértices é o comprimento da lista de adjacências

    def topologicalSortUtil(self, v, visited, stack):
        if v >= self.V:
            return
        # Marca o nó atual como visitado
        visited[v] = True

        # Recorre para todos os vértices adjacentes a este vértice
        if v in self.adj.keys():
            for node, weight in self.adj[v]:
                if node < self.V and not visited[node]:
                    self.topologicalSortUtil(node, visited, stack)

        # Adiciona o vértice atual à pilha que armazena a ordenação topológica
        stack.append(v)

    def shortestPath(self, s):
        if s >= self.V:
            raise ValueError(f"Vértice fonte {s} está fora do intervalo")

        # Marca todos os vértices como não visitados
        visited = [False] * self.V
        stack = []

        # Chama a função auxiliar recursiva para armazenar a ordenação topológica
        # começando a partir do vértice fonte
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        # Imprime a ordem topológica
        print(f"Ordem Topológica: {stack[::-1]}")

        # Inicializa as distâncias para todos os vértices como infinito e
        # a distância para a fonte como 0
        dist = [float("Inf")] * self.V
        dist[s] = 0

        # Processa os vértices na ordem topológica
        while stack:
            # Obtém o próximo vértice da ordenação topológica
            i = stack.pop()

            # Atualiza as distâncias de todos os vértices adjacentes
            for node, weight in self.adj[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight

        # Imprime a árvore de caminhos mínimos a partir do vértice fonte
        print(f"Árvore de Caminhos Mínimos a partir do vértice {s}:")
        for i in range(self.V):
            print(f"Distância do vértice {s} ao vértice {i}: {'Inf' if dist[i] == float('Inf') else dist[i]}")

def carregar_grafo(filename):
    adj = defaultdict(list)
    vertices = set()

    with open(filename, 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) == 3:
                v, w = map(int, parts[:2])  # Converte os vértices para inteiros
                weight = float(parts[2])  # Converte o peso para float
                adj[v].append((w, weight))
                vertices.add(v)
                vertices.add(w)

    # Cria um grafo com todos os vértices
    graph = Graph({v: adj[v] for v in range(max(vertices) + 1)})
    return graph


# Carregar o grafo do arquivo de texto
G = carregar_grafo('listaAdjacencias.txt')

# Aplicar o algoritmo de caminhos mais curtos a partir do vértice 0
G.shortestPath(0)
