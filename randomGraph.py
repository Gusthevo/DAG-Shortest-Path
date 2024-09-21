import random

class Grafo:
    def __init__(self, V):
        self.V = V
        self.adj = {v: [] for v in range(V)}  # Lista de adjacências para cada vértice

    def inserir_arco(self, v, w, peso):
        # Adiciona uma aresta direcionada de v para w com um peso
        self.adj[v].append((w, peso))  # Cada aresta agora é uma tupla (destino, peso)

    def mostrar_grafo(self):
        # Mostra as arestas do grafo, incluindo os pesos
        for v in range(self.V):
            print(f'Vertice {v}:', [(w, round(weight, 1)) for w, weight in self.adj[v]])

    def salvar_grafo(self, nomearquivo):
        with open(nomearquivo, 'w') as f:
            for v in self.adj:
                for w, peso in self.adj[v]:
                    f.write(f"{v} {w} {round(peso, 1)}\n")

def grafo_aleatorio(V, A, max_weight):
    prob = A / (V * (V - 1))
    G = Grafo(V)
    
    for v in range(V):
        for w in range(v + 1, V):  # Garante que w > v para evitar ciclos
            if random.random() < prob:  # Probabilidade de inserir a aresta
                peso = random.uniform(1, max_weight)  # Gera peso real aleatório entre 1 e max_weight
                G.inserir_arco(v, w, peso)

    return G

V = 100  # Número de vértices
A = 2940  # Número estimado de arestas
max_weight = 15.0  # Peso máximo das arestas (número real)

# Gerar o grafo aleatório acíclico com pesos reais e exibir
G = grafo_aleatorio(V, A, max_weight)

# Chama o método para exibir o grafo gerado
G.mostrar_grafo()
    
# Salva o grafo em um arquivo de texto
G.salvar_grafo('listaAdjacencias.txt')