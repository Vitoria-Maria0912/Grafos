import unittest
import networkx as nx
from src.Q01 import class_metrics 
from parameterized import parameterized

# Author: Patrícia Duarte de Lima Machado

# Test Data
toy1 = nx.DiGraph([('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('e', 'b')])
toy2 = nx.DiGraph([('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('e', 'b'),
                   ('d', 'b'), ('d', 'f'), ('f', 'a'), ('a', 'f')])
toy3 = nx.DiGraph([('d', 'e'), ('c', 'd'), ('a', 'c'), ('b', 'a'), ('c', 'b')])
toy4 = nx.DiGraph([('a', 'b'), ('b', 'c'), ('c', 'a'), ('b', 'a'), ('c', 'b')])
toy5 = nx.DiGraph([('x', 'y'), ('x', 'z'), ('z', 'w'), ('y', 'w'), ('x', 'x')])
toy6 = nx.DiGraph([('x', 'y')])
toy7 = nx.empty_graph(5, default=nx.DiGraph)
toy8 = nx.balanced_tree(3, 4, create_using=nx.DiGraph)
toy12 = nx.DiGraph([(0, 1), (2, 1), (3, 4), (4, 5), (5, 3), (3, 6), (6, 5)])


class TestClassMetrics(unittest.TestCase):

    @parameterized.expand([
        ["toy1-a", toy1, 'a', 2, 0],
        ["toy1-b", toy1, 'b', 1, 2],
        ["toy1-c", toy1, 'c', 2, 2],
        ["toy1-d", toy1, 'd', 0, 1],
        ["toy1-e", toy1, 'e', 1, 1],
        ["toy2-f", toy2, 'f', 1, 2],
        ["toy3-e", toy3, 'e', 0, 1],
        ["toy4-b", toy4, 'b', 2, 2],
        ["toy4-c", toy4, 'c', 2, 1],
        ["toy5-x", toy5, 'x', 3, 1],
        ["toy5-w", toy5, 'w', 0, 2],
        ["toy6-x", toy6, 'x', 1, 0],
        ["toy6-y", toy6, 'y', 0, 1],
        ["toy7-0", toy7, 0, 0, 0],
        ["toy8-4", toy8, 4, 3, 1],
        ["toy12-3", toy12, 3, 2, 1]
    ])
    def test_base(self, name, ddc, c, e_fan_out, e_fan_in):
        r_fan_out, r_fan_in = class_metrics(ddc, c)
        self.assertEqual(e_fan_out, r_fan_out, "wrong fan_out")
        self.assertEqual(e_fan_in, r_fan_in, "wrong fan_in")

    def test_None(self):
        self.assertIsNone(class_metrics(None, 0))

    def test_null(self):
        self.assertIsNone(class_metrics(nx.DiGraph(), 0))

    def test_None_Class(self):
        self.assertIsNone(class_metrics(toy1, None))

    def test_invalid_Class(self):
        self.assertIsNone(class_metrics(toy1, 'w'))

    def test_undirected_graph(self):
        self.assertIsNone(class_metrics(nx.Graph([(0, 1)]), 0))

if __name__ == '__main__':
    unittest.main(verbosity=2)
