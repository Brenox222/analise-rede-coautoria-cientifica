def dfs(grafo, vertice_inicial):
    visitados = set()
    pilha = [vertice_inicial]
    ordem_visitacao = []
    
    while pilha:
        vertice_atual = pilha.pop()
        
        if vertice_atual not in visitados:
            visitados.add(vertice_atual)
            ordem_visitacao.append(vertice_atual)
            
            for vizinho in grafo.obter_vizinhos(vertice_atual):
                if vizinho not in visitados:
                    pilha.append(vizinho)
                    
    return ordem_visitacao