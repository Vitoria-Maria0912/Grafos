import networkx as nx

# Author: Vitória Maria do Nascimento

def graph_density(g):

    if(g is None):
        return None

    has_multiple_edges = lambda g: (any(g.number_of_edges(u,v) > 1 for u in g.nodes for v in g.nodes))
    is_pseudograph = lambda g: nx.number_of_selfloops(g) > 0
    is_multigraph = lambda g: not is_pseudograph(g) and has_multiple_edges(g)

    if(is_pseudograph(g) or is_multigraph(g)):
        density = None
    
    else:
        density = float(format(nx.density(g), '.2f'))
    
    return density
