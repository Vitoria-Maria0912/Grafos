import networkx as nx

# Author: Rute Pereira da Silva

def is_candidate(G, q_list, q, t):
 
    if(G is None) or (q_list is None) or (q is None) or (t is None):
        return None
     
    if(t < 0):
        return None    
    
    if (G.number_of_nodes() == 0):
        return None
    
    if(q not in G.nodes) or (q in q_list):
        return None
    
    for v in q_list:
        if(v not in G.nodes):
            return None
         
    for vertice in q_list:
        
        if not any(n in G[q] for n in q_list):
            return False
        if not (nx.has_path(G, q, vertice)):
            return False
        if (nx.shortest_path_length(G, q, vertice, weight='weight')) > t:
            return False

    q_list.append(q)
    
    return True
