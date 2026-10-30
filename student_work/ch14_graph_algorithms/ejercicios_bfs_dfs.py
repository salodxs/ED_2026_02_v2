from goodrich.ch14.graph import Graph


def vecinos(g, v):
    """Retorna una lista con los elementos de los vecinos de v."""
    #g._incoming[v].keys()
    L=[]
    for i in g.incident_edges(v):
        L.append(i.opposite(v).element())
    return L
def vecinos_v(g, v):
    return [e.opposite(v) for e in g.incident_edges(v)]

def dfs(g, v, d):
    """DFS desde v. Agrega a d cada vertice descubierto -> arista que lo descubrio.

    v ya debe estar en d antes de la llamada (normalmente d = {v: None}). No retorna nada.
    """
    for i in vecinos_v(g, v):
        if i not in d:
            d[i] = g.get_edge(v, i)
            dfs(g, i, d)



def bfs(g, v):
    """BFS desde v. Retorna un dict vertice descubierto -> arista que lo descubrio (v -> None)."""
    d = {v: None}
    L = [v]
    while len(L) > 0:
        u = L.pop(0)
        for e in g.incident_edges(u):
            w= e.opposite(u)
            if w not in d:
                d[w] = e
                L.append(w) 
    return d


def alcanzables(g, v):
    """Retorna una lista con los elementos de los vertices alcanzables desde v (incluido v)."""
    L = []
    for w in bfs(g, v):
        L.append(w.element())
    return L


if __name__ == "__main__":
    # tus pruebas (opcional)
    pass
