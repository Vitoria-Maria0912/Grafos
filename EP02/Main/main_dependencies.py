import networkx as nx
from util.networkx_util import draw_graph
from src.Q03 import dependencies

DDC = nx.read_edgelist("datasets/toy1.elist", create_using=nx.DiGraph)
for c in DDC:
    d, i = dependencies(DDC, c)
    print(f"Class {c} - D: {d} - I: {i}")
draw_graph(DDC, nx.spring_layout(DDC))
