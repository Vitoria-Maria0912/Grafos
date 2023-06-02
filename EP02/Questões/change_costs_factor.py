import networkx as nx

# Author: Vitória Maria do Nascimento 


def change_costs_factor(ddc, c):

    # checa se os parâmetros são válidos e se o grafo é direcionado

    if(ddc == None) or (c == None) or (not nx.is_directed(ddc)) or (c not in ddc.nodes):
        return None
    
    # checa se o grau de entrada do vértice 'c' é igual a zero

    if(ddc.in_degree(c) == 0):
        return 1

    # todo grafo tem custo de manutenção 1

    fator_resultante = 0
    custo = 1
    
    sets_tangles = nx.strongly_connected_components(ddc)
    cycles = nx.simple_cycles(ddc)
    neighborhood = ddc.nodes

    # não soma se 'c' depende de 'c', ou seja, se a classe tiver loop
    # somente se outras classes são dependentes de 'c'

    for neighbor in neighborhood: 
        if(neighbor != c) and nx.has_path(ddc, neighbor, c):
            fator_resultante += 1

    # se há componentes fortes, há um tangle
    # considera-se apenas tangles > 3
    # cada tangle soma 50 ao fator resultante  
    
    for set in sets_tangles:
        if(c in set) and (len(set) > 3):
            fator_resultante += 50

    # se a classe faz parte de 1 ou mais ciclos de dependência mínimos
    # cada ciclo de dependência mínima soma 10 ao fator resultante

    for cycle in cycles:
        if(c in cycle):
            fator_resultante += 10

    # atualiza o custo somando ao fator resultante   
    
    custo += fator_resultante

    return custo


# adptação da função 'nx.minimum_cycle_basis(ddc)'
# de grafos não direcionados para grafos direcionados
def minimum_cycle_basis(grafo):

    cycles = nx.simple_cycles(grafo)

    min_cycles = []

    for cycle in cycles:

        is_subcycle = False

        for min_cycle in min_cycles:

            if set(cycle).issubset(set(min_cycle)):
                is_subcycle = True
                break
            
        if not is_subcycle:
            min_cycles.append(cycle)

    return min_cycles
