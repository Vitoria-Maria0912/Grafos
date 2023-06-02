import networkx as nx
from util.networkx_util import draw_graph
from src.Q05 import change_costs_factor

# Author: Patrícia Duarte de Lima Machado

DDC = nx.read_edgelist("datasets/toy2.elist", create_using=nx.DiGraph)

for c in DDC.nodes:
    print(f"Classe {c}: {change_costs_factor(DDC, c)}")
draw_graph(DDC, nx.kamada_kawai_layout(DDC))
