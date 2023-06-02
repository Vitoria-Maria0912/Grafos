import networkx as nx
from src.Q01 import class_metrics

# Author: Rute Pereira da Silva


# Função para identificar os vilões silenciosos
def silent_villains(ddc, threshold):

    # Verificando entradas inválidas
    if ddc is None or threshold is None or threshold < 0:
        return None

    # Verificando se o grafo de entrada é direcionado
    if not(nx.is_directed(ddc)):
        return None
    
    # Listas para armazenar os resultados
    global_breakable = []
    global_butterfly = []
    hub = []

    # Iterando sobre cada nó do grafo
    for node in ddc.nodes:
        # Calculando o grau de entrada e o grau de saída do nó
        in_degree = ddc.in_degree(node)
        out_degree = ddc.out_degree(node)

        # Verificando se o grau de entrada está acima do limite
        if in_degree > threshold:
            global_breakable.append(node)
        
        # Verificando se o grau de saída está acima do limite
        if out_degree > threshold:
            global_butterfly.append(node)
        
        # Verificando se tanto o grau de entrada quanto o grau de saída estão acima do limite
        if in_degree > threshold and out_degree > threshold:
            hub.append(node)

    # Retornando as listas de nós identificados
    return global_butterfly, global_breakable, hub
