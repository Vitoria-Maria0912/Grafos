import networkx as nx

# Author: Lucas Ariel Alves de Carvalho

def valid_word(g, s, t, w):

    vertice_inicial = s
    vertice_final = t

    if (g is None) or (w is None) or (s is None) or (t is None):
        return None

    if len(g) == 0:
        return None
    
    for letra in w:
        
        proximos_vertices = []
        
        for u, v, k in g.edges(vertice_inicial, data=True):
            try:
                if k["label"] == letra:
                    proximos_vertices.append(v)
            except:
                return None

        if len(proximos_vertices) == 0:
            return False
        
        vertice_inicial = proximos_vertices[0]

    if vertice_inicial == vertice_final:
        return True
    
    return False
