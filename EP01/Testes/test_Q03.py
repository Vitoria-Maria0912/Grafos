import unittest
import networkx as nx
from EP01.src.Q03 import graph_density
from parameterized import parameterized

# Author: Patrícia Duarte de Lima Machado

# Test Data
D1 = nx.DiGraph([(0, 1)])
D2 = nx.DiGraph()
D2.add_nodes_from(range(10))
D3 = nx.DiGraph([(0, 1), (1, 0), (1, 2), (2, 1), (0, 2), (2, 0)])
D4 = nx.DiGraph([(0, 1), (1, 0)])
D5 = nx.MultiDiGraph([(0, 1), (1, 2), (2, 0), (4, 3), (5, 6)])


class TestGraphDensity(unittest.TestCase):

    @parameterized.expand([
        # name, g, expected_result
        ["Null", nx.Graph(), 0.00],
        ["Empty", nx.empty_graph(10), 0.00],
        ["Trivial", nx.empty_graph(1), 0.00],
        ["Circle", nx.cycle_graph(9), 0.25],
        ["Petersen", nx.petersen_graph(), 0.33],
        ["D1", D1, 0.50],
        ["D2", D2, 0.00],
        ["D3", D3, 1.00],
        ["D4", D4, 1.00],
        ["D5", D5, 0.12]
    ])
    def test_base00(self, name, g, expected_result):
        result = graph_density(g)
        self.assertEqual(result, expected_result)

    def test_None(self):
        self.assertIsNone(graph_density(None))

    def test_multigraph(self):
        m = nx.MultiGraph([(0, 1), (0, 2), (0, 1)])
        self.assertIsNone(graph_density(m))

    def test_pseudograph(self):
        p = nx.MultiGraph([(0, 1), (0, 2), (0, 1)])
        self.assertIsNone(graph_density(p))


if __name__ == '__main__':
    unittest.main(verbosity=2)
