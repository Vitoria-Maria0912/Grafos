import unittest
import networkx as nx
from EP01.src.Q05 import valid_word
from util.networkx_util import draw_graph
from parameterized import parameterized

# Author: Patrícia Duarte de Lima Machado

# Test Data
A1 = nx.MultiDiGraph()
A1.add_nodes_from([0, 1, 2, 3, 4])
A1.add_edge(0, 1, label='a')
A1.add_edge(0, 1, label='e')
A1.add_edge(1, 1, label='e')
A1.add_edge(1, 2, label='i')
A1.add_edge(2, 3, label='o')
A1.add_edge(3, 3, label='o')
A1.add_edge(3, 4, label='u')
A1.add_edge(4, 4, label='u')

A2 = nx.MultiDiGraph()
A2.add_nodes_from([0, 1])
A2.add_edge(0, 0, label='a')
A2.add_edge(0, 1, label="b")

A3 = nx.MultiDiGraph()
A3.add_node(0)


class TestValidWord(unittest.TestCase):

    @parameterized.expand([
        # name, g, s, t, w, expected_result
        ["1", A1, 0, 4, "aeiou", True],
        ["2", A1, 0, 4, "eiou", True],
        ["3", A1, 0, 4, "aaaaaeiou", False],
        ["4", A1, 0, 4, "aeeeeeiou", True],
        ["5", A1, 0, 4, "aeeeeeiou", True],
        ["6", A1, 0, 4, "aeiiiiou", False],
        ["6", A1, 0, 4, "aeooooou", False],
        ["7", A1, 0, 4, "aeiooooou", True],
        ["8", A2, 0, 1, "b", True],
        ["9", A2, 0, 1, "aaaaa", False],
        ["10", A2, 0, 1, "aaaaab", True],
        ["11", A3, 0, 0, "qualquer", False],
        ["12", A3, 0, 0, "", True]
    ])
    def test_base00(self, name, g, s, t, w, expected_result):
        result = valid_word(g, s, t, w)
        self.assertEqual(result, expected_result)

    def test_None(self):
        self.assertTrue(valid_word(None, 0, 1, "qualquer") is None)

    def test_null(self):
        self.assertTrue(valid_word(nx.MultiDiGraph(), 0, 1, "qualquer") is None)

    def test_states(self):
        self.assertTrue(valid_word(A3, None, 1, "qualquer") is None)
        self.assertTrue(valid_word(A3, 0, None, "qualquer") is None)

    def test_None_word(self):
        self.assertTrue(valid_word(A3, 0, 1, None) is None)

    def test_invalid_states(self):
        self.assertTrue(valid_word(A3, 20, 1, None) is None)
        self.assertTrue(valid_word(A3, 0, 20, None) is None)

    def test_graph_without_edge_labels(self):
        g = nx.MultiDiGraph()
        g.add_nodes_from([0, 1, 2])
        g.add_edges_from([(0, 1), (1, 2)])
        self.assertTrue(valid_word(g, 0, 2, "qualquer") is None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
