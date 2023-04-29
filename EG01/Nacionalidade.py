import networkx as nx

# Author: Pedro Henrique Sarmento Pereira

def associate_astronauts(list_a):
        
        if(list_a == None):
            return None
        elif (len(list_a) == 0):
            return nx.Graph()
        
        fork = adicionando_vertices(list_a)
        
        if(len(fork) != 0):
            for i  in range(len(fork)):
                for j in range(i + 1, len(fork)):
                    if(fork.nodes[i]['country'] != fork.nodes[j]['country'] and not (fork.has_edge(i,j))):
                        fork.add_edge(i,j)
            return fork


def adicionando_vertices(list_a):
        
    fork = nx.Graph()

    for i in range(len(list_a)):
        if(list_a[i] != None and type(list_a[i]) is tuple and len(list_a[i]) == 3):
            fork.add_node(i)
            attrs = {i: {'first_name': list_a[i][0], 'last_name': list_a[i][1], 'country': list_a[i][2]}}
            nx.set_node_attributes(fork, attrs)  
        
    return fork
