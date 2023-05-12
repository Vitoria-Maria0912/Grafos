import networkx as nx

# Author: Vinícius José Soares Barbosa 

def best_route (G,i):
    
    if G is None or i is None:
        return None

    if i not in G.nodes:
        return None
    
    for v in G.nodes:
        if v not in nx.get_node_attributes(G, 'depth'):
            return None
        
        if v not in nx.get_node_attributes(G, 'full'):
            return None
    
    if G.nodes[i]['depth'] != 0:
        return None
    
    if G.nodes[i]['full'] == True:
        return []
    
    route = [i]
    current_depth = G.nodes[i]["depth"]
    
    while not all(G.nodes[v]["full"] for v in route):

        valid_neighbors = [n for n in G.neighbors(route[-1])
        if not G.nodes[n]["full"] and G.nodes[n]["depth"] > current_depth and n not in route]
        
        if not valid_neighbors:
            break

        next_vertex = min(valid_neighbors, key=lambda n: G.nodes[n]["depth"])
        route.append(next_vertex)
        current_depth = G.nodes[next_vertex]["depth"]
    
    return route
