import unittest
import networkx as nx
from src.Q05 import change_costs_factor 
from parameterized import parameterized

# Test Data
toy1 = nx.DiGraph([('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('e', 'b')])
toy2 = nx.DiGraph(
    [('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('e', 'b'), ('d', 'b'), ('d', 'f'), ('f', 'a'),
     ('a', 'f')])
toy3 = nx.DiGraph([('d', 'e'), ('c', 'd'), ('a', 'c'), ('b', 'a'), ('c', 'b')])
toy4 = nx.DiGraph([('a', 'b'), ('b', 'c'), ('c', 'a'), ('b', 'a'), ('c', 'b')])
toy5 = nx.DiGraph([('x', 'y'), ('x', 'z'), ('z', 'w'), ('y', 'w'), ('x', 'x')])
toy6 = nx.DiGraph([('x', 'y')])
toy7 = nx.DiGraph([(0, 1), (0, 10), (0, 0), (0, 0), (0, 0), (0, 3), (1, 2), (1, 2), (1, 2), (1, 4), (1, 12),
                   (2, 0), (2, 0), (3, 1), (3, 4), (3, 4), (4, 2), (5, 0), (5, 2), (5, 13), (6, 0), (6, 0),
                   (7, 3), (7, 14), (7, 0), (8, 1), (8, 1), (8, 0), (9, 0), (9, 4), (11, 0), (12, 12), (15, 4),
                   (16, 1), (17, 2), (18, 3), (19, 3)])
toy8 = nx.empty_graph(4, default=nx.DiGraph)
toy9 = nx.balanced_tree(2, 3, create_using=nx.DiGraph)
toy10 = nx.binomial_tree(4, create_using=nx.DiGraph)
nx.add_cycle(toy10, [4, 7, 9, 1])
toy12 = nx.DiGraph([(0, 1), (2, 1), (3, 4), (4, 5), (5, 3), (3, 6), (6, 5)])

# Author: Patrícia Duarte de Lima Machado

class TestChangeCostsFactor(unittest.TestCase):

    @parameterized.expand([
        ["toy1-a", toy1, 'a', 1],
        ["toy1-b", toy1, 'b', 14],
        ["toy1-d", toy1, 'd', 5],
        ["toy2-c", toy2, 'c', 96],
        ["toy2-d", toy2, 'd', 86],
        ["toy2-e", toy2, 'e', 66],
        ["toy3-c", toy3, 'c', 13],
        ["toy3-e", toy3, 'e', 5],
        ["toy4-b", toy4, 'b', 33],
        ["toy4-a", toy4, 'a', 23],
        ["toy5-x", toy5, 'x', 11],
        ["toy5-w", toy5, 'w', 4],
        ["toy6-x", toy6, 'x', 1],
        ["toy6-y", toy6, 'y', 2],
        ["toy7-1", toy7, 1, 106],
        ["toy7-13", toy7, 13, 2],
        ["toy8", toy8, 0, 1],
        ["toy9-0", toy9, 1, 2],
        ["toy9-9", toy9, 13, 4],
        ["toy10-0", toy10, 0, 1],
        ["toy10-1", toy10, 7, 77],
        ["toy12-4", toy12, 4, 64]
    ])
    def test_base(self, name, ddc, c, expected_result):
        # print(ddc.nodes)
        # print(c)
        result = change_costs_factor(ddc, c)
        self.assertEqual(expected_result, result)

    def test_None(self):
        self.assertIsNone(change_costs_factor(None, 0))

    def test_null(self):
        self.assertIsNone(change_costs_factor(nx.DiGraph(), 0))

    def test_None_Class(self):
        self.assertIsNone(change_costs_factor(toy1, None))

    def test_invalid_Class(self):
        self.assertIsNone(change_costs_factor(toy1, 'w'))

    def test_undirected_graph(self):
        self.assertIsNone(change_costs_factor(nx.Graph([(0, 1)]), 0))

if __name__ == '__main__':
    unittest.main(verbosity=2)
