import time
import matplotlib.pyplot as plt
from main import carregar_grafo

# Função para medir o tempo de execução do algoritmo de caminhos mais curtos
def medir_tempo_dag(filename, source_vertex):
    G = carregar_grafo(filename)
    
    start_time = time.time()
    G.shortestPath(source_vertex)
    end_time = time.time()

    return (end_time - start_time) * 1000  # Retorna o tempo em milissegundos

filename = 'listaAdjacencias.txt'
vertice_fonte = 0
num_testes = 10
tempos_execucao = []

# Medindo o tempo de execução
for i in range(num_testes): 
    tempo = medir_tempo_dag(filename, vertice_fonte)
    tempos_execucao.append(tempo)

# Calcula a média dos tempos após as execuções
tempo_medio = sum(tempos_execucao) / num_testes

# Mostrar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_testes + 1), tempos_execucao, marker='o', color='darkblue')
plt.axhline(y=tempo_medio, color='r', linestyle='--', label=f'Tempo Médio: {tempo_medio:.2f} ms')
plt.xlabel('Execução')
plt.ylabel('Tempo (milissegundos)')
plt.title('Tempo de Execução do Algoritmo DAG Shortest Paths')
plt.legend()
plt.grid(True)
plt.show()
