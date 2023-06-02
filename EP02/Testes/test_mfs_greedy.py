import unittest
import networkx as nx
from src.Q04 import mfs_greedy 
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
toy7 = nx.DiGraph()
toy8 = nx.empty_graph(5, default=nx.DiGraph)
toy9 = nx.balanced_tree(2, 3, create_using=nx.DiGraph)
toy10 = nx.binomial_tree(4, create_using=nx.DiGraph)
nx.add_cycle(toy10, [4, 7, 9, 1])
toy11 = nx.complete_graph(5, create_using=nx.DiGraph)
toy12 = nx.DiGraph([(0, 1), (2, 1), (3, 4), (4, 5), (5, 3), (3, 6), (6, 5)])


class TestMFSGreedy(unittest.TestCase):

    @parameterized.expand([
        ['toy1', toy1, [('c', 'e')]],
        ['toy2', toy2, [('c', 'd'), ('a', 'f'), ('c', 'e')]],
        ['toy3', toy3, [('c', 'b')]],
        ['toy4', toy4, [('b', 'c'), ('b', 'a')]],
        ['toy5', toy5, [('x', 'x')]],
        ['toy6', toy6, []],
        ['toy7', toy7, []],
        ['toy8', toy8, []],
        ['toy9', toy9, []],
        ['toy10', toy10, [(9, 1)]],
        ['toy11', toy11, [(4, 3), (4, 2), (4, 1), (4, 0), (3, 2), (3, 1), (3, 0), (2, 1), (2, 0), (1, 0)]],
        ['toy12', toy12, [(5, 3)]]
    ])
    def test_base(self, name, ddc, expected_result):
        self.assertCountEqual(mfs_greedy(ddc), expected_result)

    def test_None(self):
        self.assertIsNone(mfs_greedy(None))

    def test_undirected_graph(self):
        self.assertIsNone(mfs_greedy(nx.Graph([(0, 1)])))

if __name__ == '__main__':
    unittest.main(verbosity=2)
