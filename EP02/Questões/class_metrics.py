import networkx as nx

# Author: Pedro Henrique Sarmento Pereira

def class_metrics(ddc, c):
    
    # Checa se os parâmetros são válidos e se o grafo é direcionado
    
    if(ddc is None) or (c is None) or (c not in ddc) or not(nx.is_directed(ddc)):
        return None
    
    return (ddc.out_degree(c),ddc.in_degree(c))
