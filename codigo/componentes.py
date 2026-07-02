from codigo.bfs import bfs

def encontrar_componentes_conexas(grafo):
    visitados = set()
    componentes = []
    
    todos_professores = grafo.obter_todos_vertices()
    
    for professor in todos_professores:
        
        if professor not in visitados:
            membros_do_grupo = bfs(grafo, professor)
            
            componentes.append(membros_do_grupo)

            for p in membros_do_grupo:
                visitados.add(p)
                
    return componentes