import networkx as nx
from util.networkx_util import draw_graph
from src.Q06 import class_order

DDC = nx.read_edgelist("datasets/toy1.elist", create_using=nx.DiGraph)

generations = class_order(DDC)
print(generations)
draw_graph(DDC, nx.spring_layout(DDC))