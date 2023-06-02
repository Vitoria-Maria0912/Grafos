import networkx as nx
from util.networkx_util import draw_graph
from src.Q02 import silent_villains

DDC = nx.read_edgelist("datasets/toy1.elist", create_using=nx.DiGraph)

g_br, g_bu, h = silent_villains(DDC, 1)
print(f"Global Breakable: {g_br}")
print(f"Global Butterfly: {g_bu}")
print(f"Hub: {h}")
draw_graph(DDC, nx.spring_layout(DDC))
