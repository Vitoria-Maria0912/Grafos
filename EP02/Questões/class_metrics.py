import networkx as nx

# Author: Pedro Henrique Sarmento Pereira


def class_metrics(ddc, c):

    # verifica se os parâmetros são válidos e se o grafo é direcionadp.
    
    if(ddc is None or c is None or c not in ddc or not nx.is_directed(ddc)):
        return None
    
    # retorna uma tupla com o número de vértices que o vértice 'c', pertencente a ddc, depende.
    # e o número de vértices que dependem do vértice 'c', pertencente a ddc.
    
    return (ddc.out_degree(c),ddc.in_degree(c))
