import networkx as nx
from src.Q04 import mfs_greedy

# Author: Vitória Maria do Nascimento 


def class_order(ddc):

    # verifica se o grafo é válido
    if(ddc is None) or (not nx.is_directed(ddc)):
        return None
    
    # verifica se o grafo é acíclico
    if nx.is_directed_acyclic_graph(ddc):

        # inverte a ordem topológica
        ordered_nodes = list(nx.topological_generations(ddc))
        ordered_nodes.reverse()
        
    # se o grafo for cíclico importa a função 'mfs_greedy', da questão 4, para 'remover' os ciclos e torná-lo acíclico
    else:

        mfs = mfs_greedy(ddc)

        # faz uma cópia do grafo, para remover as arestas do MFS
        ddc_without_mfs = ddc.copy()
        
        # remove todas as arestas correspondentes ao MFS
        for edge in mfs:
            ddc_without_mfs.remove_edge(*edge)
        
        # inverte a ordem topológica, sem o MFS
        ordered_nodes = list(nx.topological_generations(ddc_without_mfs))
        ordered_nodes.reverse()
    
    return ordered_nodes
        