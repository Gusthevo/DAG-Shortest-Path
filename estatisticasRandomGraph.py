import time
import matplotlib.pyplot as plt
import randomGraph
from randomGraph import grafo_aleatorio

# Parâmetros do grafo
num_tests = 10  # Número de testes por configuração
num_graphs = 10  # Número de grafos aleatórios que será gerado
V = randomGraph.V  # Número de vértices vindo do outro arquivo
A = randomGraph.A  # Número estimado de arestas também vindo do outro arquivo
max_weight = randomGraph.max_weight  # Peso máximo das arestas também vindo outro arquivo

tempos_execucao = []

# Medindo o tempo de geração do grafo em várias execuções
for i in range(num_graphs):
    tempos_testes = []
    
    for j in range(num_tests):  # Corrigido o loop interno para não repetir a variável 'i'
        inicio = time.time()
        G = grafo_aleatorio(V, A, max_weight)
        fim = time.time()
        
        # Convertendo o tempo para milissegundos
        tempos_testes.append((fim - inicio) * 1000)

    # Calcula a média dos tempos para essa configuração
    tempo_medio = sum(tempos_testes) / num_tests
    tempos_execucao.append(tempo_medio)

# Calcula a média geral dos tempos de execução
tempo_medio_geral = sum(tempos_execucao) / num_graphs

# Mostrando o gráfico dos tempos de execução
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_graphs + 1), tempos_execucao, marker='o', color='darkblue')
plt.axhline(y=tempo_medio_geral, color='r', linestyle='--', label=f'Tempo Médio Geral: {tempo_medio_geral:.2f} ms')
plt.xlabel('Grafo Aleatório')
plt.ylabel('Tempo Médio (milissegundos)')
plt.title('Tempo Médio de Geração de Grafos Aleatórios')
plt.legend()
plt.grid(True)
plt.show()
