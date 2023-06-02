import unittest
import networkx as nx
from src.Q02 import silent_villains 
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
toy8 = nx.balanced_tree(2, 3, create_using=nx.DiGraph)
toy9 = nx.DiGraph()
toy12 = nx.DiGraph([(0, 1), (2, 1), (3, 4), (4, 5), (5, 3), (3, 6), (6, 5)])


class TestSilentVillains(unittest.TestCase):

    @parameterized.expand([
        ['toy1-0', toy1, 0, ['a', 'b', 'c', 'e'], ['d', 'b', 'c', 'e'], ['b', 'e', 'c']],
        ['toy1-1', toy1, 1, ['c', 'a'], ['b', 'c'], ['c']],
        ['toy1-10', toy1, 10, [], [], []],
        ['toy2-0', toy2, 0, ['a', 'b', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'd', 'e', 'f'],
                            ['a', 'b', 'c', 'd', 'e', 'f']],
        ['toy2-2', toy2, 2, ['a'], ['b'], []],
        ['toy2-2', toy2, 4, [], [], []],
        ['toy3-0', toy3, 0, ['d', 'c', 'a', 'b'], ['d', 'e', 'c', 'a', 'b'], ['d', 'c', 'a', 'b']],
        ['toy3-1', toy3, 1, ['c'], [], []],
        ['toy4-1', toy4, 0, ['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']],
        ['toy4-2', toy4, 1, ['b', 'c'], ['a', 'b'], ['b']],
        ['toy5-1', toy5, 1, ['x'], ['w'], []],
        ['toy5-0', toy5, 0, ['x', 'y', 'z'], ['x', 'y', 'z', 'w'], ['x', 'y', 'z']],
        ['toy6_0', toy6, 1, [], [], []],
        ['toy6_0', toy6, 0, ['x'], ['y'], []],
        ['toy7_0', toy7, 0, [], [], []],
        ['toy8_3', toy8, 1, [0, 1, 2, 3, 4, 5, 6], [], []],
        ['toy9-9', toy9, 9, [], [], []],
        ['toy12-0', toy12, 0, [0, 2, 3, 4, 5, 6], [1, 3, 4, 5, 6], [3, 4, 5, 6]],
        ['toy12-1', toy12, 1, [3], [1, 5], []]
    ])
    def test_base(self, name, ddc, threshold, e_global_breakable, e_global_butterfly, e_hub):
        r_global_breakable, r_global_butterfly, r_hub = silent_villains(ddc, threshold)
        self.assertCountEqual(e_global_breakable, r_global_breakable, "wrong global breakable list")
        self.assertCountEqual(e_global_butterfly, r_global_butterfly, "wrong global butterfly list")
        self.assertCountEqual(e_hub, r_hub, "wrong hub list")

    def test_None(self):
        self.assertIsNone(silent_villains(None, 0))

    def test_None_threshold(self):
        self.assertIsNone(silent_villains(toy1, None))

    def test_invalid_threshold(self):
        self.assertIsNone(silent_villains(toy1, -1))

    def test_undirected_graph(self):
        self.assertIsNone(silent_villains(nx.Graph([(0, 1)]), 0))

if __name__ == '__main__':
    unittest.main(verbosity=2)
