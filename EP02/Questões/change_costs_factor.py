import networkx as nx


def change_costs_factor(ddc, c):

    # todo grafo tem custo de manutenção 1

    fator_resultante = 0
    custo = 1

    if(ddc == None or c == None):
        return custo
    
    sem_loop = True

    # verifica se há loop no vértice 'c'

    for node in nx.nodes_with_selfloops(ddc):
        if(node == c):
            sem_loop = False

    # não soma se 'c' depende de 'c', ou seja, se 'c' tiver loop
    # somente se outras classes são dependentes de 'c'

    if(nx.neighborns(ddc, c) != None) and (sem_loop) and (ddc.in_degree(c) > 0):

        fator_resultante += 1

        # se há componentes fortes, há um tangle
        # considera-se apenas tangles > 3  
        # checar se há componentes fortes do 'node' até alguém ----------------------------------------------
        if(a classe faz parte de um tangle):
            fator_resultante += 50

        # o que seria um ciclo de dependência mínima? --------------------------------------------------------
        if(a classe faz parte de 1 ou
            mais ciclos de dependência mínimos):
            fator_resultante += 10

    custo += fator_resultante

    return custo
