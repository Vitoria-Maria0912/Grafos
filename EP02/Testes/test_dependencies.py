import unittest
import networkx as nx
from src.Q03 import dependencies 
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
toy12 = nx.DiGraph([(0, 1), (2, 1), (3, 4), (4, 5), (5, 3), (3, 6), (6, 5)])


class TestDependencies(unittest.TestCase):

    @parameterized.expand([
        ["toy1-a", toy1, 'a', ['b', 'c'], ['d', 'e']],
        ["toy1-b", toy1, 'b', ['c'], ['d', 'e']],
        ["toy1-c", toy1, 'c', ['d', 'e'], ['b']],
        ["toy1-d", toy1, 'd', [], []],
        ["toy1-e", toy1, 'e', ['b'], ['c', 'd']],
        ["toy2-c", toy2, 'c', ['d', 'e'], ['b', 'f', 'a']],
        ["toy2-f", toy2, 'f', ['a'], ['b', 'c', 'd', 'e']],
        ["toy2-a", toy2, 'a', ['b', 'c', 'f'], ['d', 'e']],
        ["toy3-c", toy3, 'c', ['d', 'b'], ['a', 'e']],
        ["toy4-b", toy4, 'b', ['a', 'c'], []],
        ["toy4-a", toy4, 'a', ['b'], ['c']],
        ["toy5-x", toy5, 'x', ['x', 'z', 'y'], ['w']],
        ["toy5-w", toy5, 'w', [], []],
        ["toy6-x", toy6, 'x', ['y'], []],
        ["toy6-y", toy6, 'y', [], []],
        ["toy7-0", toy7, 0, [], []],
        ["toy8-0", toy8, 0, [1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
        ["toy12-3", toy12, 3, [4, 6], [5]]
    ])
    def test_base(self, name, ddc, c, e_d_dep, e_i_dep):
        r_d_dep, r_i_dep = dependencies(ddc, c)
        self.assertCountEqual(e_d_dep, r_d_dep, "wrong direct dependencies")
        self.assertCountEqual(e_i_dep, r_i_dep, "wrong indirect dependencies")

    def test_None(self):
        self.assertIsNone(dependencies(None, 0))

    def test_None_Class(self):
        self.assertIsNone(dependencies(toy1, None))

    def test_invalid_Class(self):
        self.assertIsNone(dependencies(toy1, 'w'))

    def test_undirected_graph(self):
        self.assertIsNone(dependencies(nx.Graph([(0, 1)]), 0))

if __name__ == '__main__':
    unittest.main(verbosity=2)