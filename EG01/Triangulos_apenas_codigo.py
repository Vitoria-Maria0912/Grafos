#@title  { run: "auto", vertical-output: true }
filename1 = "s-u-cy-sc-p-06.graphml" #@param ["m-u-cy-sc-p-01.graphml", "p-u-cy-sc-p-ch-01.graphml", "s-u-cy-sc-p-01.graphml", "s-u-cy-sc-p-05.graphml", "s-u-a-sc-p-t-b-03.graphml", "s-u-cy-sc-p-06.graphml", "s-u-cy-sc-p-b-01.graphml", "s-u-cy-sc-p-03.graphml", "K3-3.graphml", "Cycle6.graphml", "Empty6.graphml"]
layout1 = "spring_layout" #@param ["circular_layout", "kamada_kawai_layout", "planar_layout", "random_layout", "shell_layout", "spring_layout", "spectral_layout", "spiral_layout"]

def triangles (G):
  
  lista = []
  
  if G is None:
    return None

  if G.number_of_nodes() <= 2:
    return lista

  nodes = list(G.nodes)
  
  for u in range(len(G.nodes)):
    for v in range(u+1, len(G.nodes)):
      for w in range(u+2, len(G.nodes)):
        if G.has_edge(nodes[u],nodes[v]) and G.has_edge(nodes[v],nodes[w]) and G.has_edge(nodes[w],nodes[u]):
          lista.append([nodes[u], nodes[v], nodes[w]])

  for u in range(len(lista) - 2, -1, -1):
    lista[u].sort()
    lista[u+1].sort()
    if lista[u] == lista[u+1]:
      lista.remove(lista[u])

  return lista


# Exemplo de uso da função
G1 = nx.read_graphml(filename1)
draw_graph(G1,eval(f"nx.{layout1}(G1)"))
print(f"Vértices: {G1.nodes}")
print(f"Arestas: {G1.edges}\n") 
print(triangles(G1))
