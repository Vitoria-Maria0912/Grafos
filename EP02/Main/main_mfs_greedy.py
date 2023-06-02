import networkx as nx
from util.networkx_util import draw_graph
from src.Q04 import mfs_greedy

# Author: Patrícia Duarte de Lima Machado

DDC = nx.read_edgelist("datasets/toy2.elist", create_using=nx.DiGraph)
print(mfs_greedy(DDC))
draw_graph(DDC,nx.spring_layout(DDC))