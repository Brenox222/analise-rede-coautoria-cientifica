from collections import deque

def bfs(grafo, vertice_inicial):
    visitados = set()
    fila = deque([vertice_inicial])
    ordem_visitacao = []
    
    visitados.add(vertice_inicial)
    
    while fila:
        vertice_atual = fila.popleft()
        ordem_visitacao.append(vertice_atual)
        
        for vizinho in grafo.obter_vizinhos(vertice_atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                
    return ordem_visitacao