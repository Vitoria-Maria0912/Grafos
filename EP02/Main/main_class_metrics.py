import networkx as nx
from util.networkx_util import draw_graph
from src.Q01 import class_metrics

DDC = nx.read_edgelist("datasets/toy1.elist", create_using=nx.DiGraph)
for c in DDC:
    fan_out, fan_in = class_metrics(DDC, c)
    print(f"class: {c} fan_out: {fan_out} fan_in: {fan_in}")
draw_graph(DDC, nx.spring_layout(DDC))
