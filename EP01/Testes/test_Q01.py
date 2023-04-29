import unittest
from EP01.src.Q01 import associate_astronauts
from parameterized import parameterized

# Author: Patrícia Duarte de Lima Machado

class TestAstronauts(unittest.TestCase):

    @parameterized.expand([
        # name, alist, expected_nodes, expected_edges
        ['One Person', [('f1', 'l1', 'c1')], [0], []],
        ['One Country', [('f1', 'l1', 'c'), ('f2', 'l2', 'c'), ('f3', 'l3', 'c')], [0, 1, 2], []],
        ['All Diff Country', [('f1', 'l1', 'c1'), ('f2', 'l2', 'c2'), ('f3', 'l3', 'c3')], [0, 1, 2],
         [(0, 1), (1, 2), (2, 0)]],
        ['Misc1', [('Kurtis', 'Shepstone', 'Italy'),
                   ('Rafferty', 'Stoak', 'Canada'),
                   ('Libbey', 'Anselm', 'Canada'),
                   ('Odelinda', 'Thireau', 'Italy'),
                   ('Rick', 'Caset', 'Canada'),
                   ('Matthew', 'Fearnyough', 'Canada'),
                   ('Madonna', 'Brazener', 'Canada'),
                   ('Laure', 'Drohane', 'Canada'),
                   ('Eleanore', 'Pollett', 'USA'),
                   ('Town', 'Duddell', 'Canada')], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
         [(0, 1), (0, 2), (0, 4), (0, 5), (0, 6), (7, 0), (0, 8), (0, 9), (1, 3), (1, 8), (2, 3), (2, 8), (3, 4),
          (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 8), (5, 8), (6, 8), (7, 8), (8, 9)]],
        ['Misc2', [('Kurtis', 'Shepstone', 'Italy'),
                   ('Rafferty', 'Stoak', 'Canada'),
                   ('Libbey', 'Anselm', 'Canada'),
                   ('Odelinda', 'Thireau', 'Italy'),
                   ('Eleanore', 'Pollett', 'USA'),
                   ('Town', 'Duddell', 'Canada')], [0, 1, 2, 3, 4, 5],
         [(0, 1), (0, 2), (0, 4), (0, 5), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]],
        ['Empty', [], [], []]
    ])
    def test_base00(self, name, alist, expected_nodes, expected_edges):
        g = associate_astronauts(alist)
        # print(G.nodes)
        # print(G.edges)
        self.assertCountEqual(g.nodes, expected_nodes)
        self.assertTrue(all(g.has_edge(u, v) for u, v in expected_edges))

    def test_None(self):
        self.assertIsNone(associate_astronauts(None))

    def test_Invalid_list1(self):
        self.assertIsNone(associate_astronauts([0, 1, 2]))

    def test_Invalid_list2(self):
        self.assertIsNone(associate_astronauts([(0, 1), (2, 3)]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
