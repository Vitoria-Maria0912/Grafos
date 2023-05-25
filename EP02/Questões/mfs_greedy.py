import networkx as nx
from src.Q01 import class_metrics

# Author: Lucas Ariel Alves de Carvalho


def mfs_greedy(ddc):
    # Verifica se o grafo fornecido é válido
    if (ddc is None) or (not nx.is_directed(ddc)):
        return None

    # Encontra os ciclos mínimos de dependência no grafo
    md_cycles = encontrar_ciclos_minimos_dependencia(ddc)

    mfs = []  # Lista para armazenar as arestas do MFS

    while md_cycles:
        max_ocorrencias = 0  # Número máximo de ocorrências de uma aresta
        max_arco = None  # Aresta com o número máximo de ocorrências

        for ciclo in md_cycles:
            for arco in ciclo:
                ocorrencias = sum(1 for c in md_cycles if arco in c)  # Conta o número de ocorrências da aresta no ciclo
                # Verifica se a aresta tem mais ocorrências ou se há empate e utiliza a função "comparar_arcos" para desempatar
                if ocorrencias > max_ocorrencias or (ocorrencias == max_ocorrencias and comparar_arcos(arco, max_arco, ddc)):
                    max_ocorrencias = ocorrencias
                    max_arco = arco

        mfs.append(max_arco)  # Adiciona a aresta com o maior número de ocorrências ao MFS

        md_cycles = [ciclo for ciclo in md_cycles if max_arco not in ciclo]  # Remove os ciclos que contêm a aresta selecionada

    return mfs


def encontrar_ciclos_minimos_dependencia(ddc):
    arcos_ciclos = []  # Lista para armazenar as arestas dos ciclos mínimos de dependência
    ciclos = []  # Lista para armazenar os ciclos mínimos de dependência

    def dfs(no, visitados, caminho):
        visitados.add(no)
        caminho.append(no)

        for vizinho in ddc[no]:
            if vizinho in caminho:
                indice_vizinho = caminho.index(vizinho)
                ciclo = caminho[indice_vizinho:]
                if ciclo not in ciclos:  # Evita ciclos duplicados
                    ciclos.append(ciclo)
            elif vizinho not in visitados:
                dfs(vizinho, visitados, caminho)

        caminho.pop()
        visitados.remove(no)

    visitados = set()

    for node in ddc:
        if node not in visitados:
            dfs(node, visitados, [])

    for ciclo in ciclos:
        # Verifica se o ciclo é completo
        if len(ciclo) < len(ddc) and len(set(ciclo)) == len(ciclo):
            arcos_ciclo = [(ciclo[i], ciclo[i + 1]) for i in range(len(ciclo) - 1)]
            arco_final = (ciclo[-1], ciclo[0])
            arcos_ciclo.append(arco_final)
            arcos_ciclos.append(arcos_ciclo)

    return arcos_ciclos


def comparar_arcos(arco1, arco2, ddc):
    inicio1, fim1 = arco1
    inicio2, fim2 = arco2

    fan_out1 = len(list(ddc.successors(inicio1)))  # Número de nós de saída do nó de início da primeira aresta
    fan_out2 = len(list(ddc.successors(inicio2)))  # Número de nós de saída do nó de início da segunda aresta
    fan_in1 = len(list(ddc.predecessors(inicio1)))  # Número de nós de entrada do nó de início da primeira aresta
    fan_in2 = len(list(ddc.predecessors(inicio2)))  # Número de nós de entrada do nó de início da segunda aresta

    # Compara os números de nós de saída e entrada e, em caso de empate, compara os nós lexicograficamente
    if fan_out1 > fan_out2:
        return True
    elif fan_out1 == fan_out2:
        if fan_in1 > fan_in2:
            return True
        elif fan_in1 == fan_in2:
            return (inicio1, fim1) > (inicio2, fim2)

    return False
