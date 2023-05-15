import networkx as nx


def change_costs_factor(ddc, c):
    
    fator_resultante = 0
    custo = 1
    
    for(dependentes: ddc):

    # não soma se c depende de c
    if(outras classes são dependentes de c):
        fator_resultante += 1

    if(a classe faz parte de um tangle):
        fator_resultante += 50

    if(a classe faz parte de 1 ou
        mais ciclos de dependência mínimos):
        fator_resultante += 10

    return custo + fator_resultante
