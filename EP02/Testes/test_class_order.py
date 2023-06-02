import unittest
import networkx as nx
from src.Q06 import class_order 
from parameterized import parameterized

# Author: Patrícia Duarte de Lima Machado

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
toy8 = nx.empty_graph(5, default=nx.DiGraph)
toy9 = nx.balanced_tree(2, 3, create_using=nx.DiGraph)
toy10 = nx.binomial_tree(4, create_using=nx.DiGraph)
nx.add_cycle(toy10, [4, 7, 9, 1])
toy11 = nx.DiGraph()
toy12 = nx.DiGraph([(0, 1), (2, 1), (3, 4), (4, 5), (5, 3), (3, 6), (6, 5)])


class Test_class_order(unittest.TestCase):

    @parameterized.expand([
        ["toy1", toy1, [['d'], ['c'], ['b'], ['a', 'e']]],
        ["toy2", toy2, [['c'], ['b'], ['a'], ['f'], ['d', 'e']]],
        ["toy3", toy3, [['e'], ['d'], ['c'], ['a'], ['b']]],
        ["toy4", toy4, [['b'], ['a'], ['c']]],
        ["toy5", toy5, [['w'], ['y', 'z'], ['x']]],
        ["toy6", toy6, [['y'], ['x']]],
        ["toy7", toy7, [[2], [4, 12], [1], [10, 3], [13, 14, 0], [5, 6, 7, 8, 9, 11, 15, 16, 17, 18, 19]]],
        ["toy8", toy8, [[0, 1, 2, 3, 4]]],
        ["toy9", toy9, [[7, 8, 9, 10, 11, 12, 13, 14], [3, 4, 5, 6], [1, 2], [0]]],
        ["toy10", toy10, [[9], [7, 15], [5, 6, 11, 13, 14], [4, 3, 10, 12], [1, 2, 8], [0]]],
        ["toy11", toy11, []],
        ["toy12", toy12, [[5], [1, 4, 6], [0, 2, 3]]]
    ])
    def test_base(self, name, ddc, expected_result):
        result = class_order(ddc)
        self.assertEqual(expected_result, result)

    def test_None(self):
        self.assertIsNone(class_order(None))

    def test_undirected_graph(self):
        self.assertIsNone(class_order(nx.Graph([(0, 1)])))

if __name__ == '__main__':
    unittest.main(verbosity=2)
