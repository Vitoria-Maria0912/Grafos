import unittest
import networkx as nx
from EP01.src.Q02 import is_candidate
from parameterized import parameterized
from collections import Counter

# Author: Patrícia Duarte de Lima Machado

# TEST DATA
S1 = ["n0 n1 2", "n0 n2 3", "n1 n2 1", "n3 n4 4"]
G1 = nx.parse_edgelist(S1, data=(("weight", int),))
S2 = ['n0 n1 1', 'n0 n3 5', 'n1 n3 2', 'n1 n6 4', 'n1 n4 6', 'n2 n5 3', 'n2 n4 8']
G2 = nx.parse_edgelist(S2, data=(("weight", int),))
# .graphs/s-u-w-cy-sc-p-01.graphml
S3 = ['n0 n1 120', 'n0 n6 300', 'n0 n5 250', 'n1 n2 80', 'n1 n6 250', 'n2 n3 150', 'n2 n7 280', 'n3 n4 100',
      'n3 n8 250', 'n4 n9 250', 'n5 n6 120', 'n5 n10 150', 'n6 n11 150', 'n6 n7 150', 'n7 n12 260', 'n7 n8 80',
      'n8 n9 100', 'n9 n12 180', 'n10 n11 120']
G3 = nx.parse_edgelist(S3, data=(("weight", int),))


class TestIsCandidate(unittest.TestCase):

    @parameterized.expand([
        # name, G, q_list, q, t, expected_result
        ['0', G1, ['n1', 'n2', 'n0'], 'n3', 4, False],
        ['1', G1, ['n0', 'n1'], 'n2', 10, True],
        ['2', G1, ['n0', 'n1'], 'n2', 2, False],
        ['3', G1, ['n0', 'n1'], 'n2', 0, False],
        ['4', G1, ['n3'], 'n4', 6, True],
        ['5', G1, ['n3'], 'n4', 2, False],
        ['6', G2, ['n0', 'n1', 'n3'], 'n6', 10, True],
        ['7', G2, ['n0', 'n1', 'n3'], 'n6', 5, False],
        ['8', G2, ['n2', 'n1', 'n4'], 'n6', 12, False],
        ['9', G2, ['n2', 'n1', 'n4'], 'n6', 20, True],
        ['10', G2, ['n4', 'n1', 'n0', 'n3'], 'n5', 40, False],
        ['11', G3, ['n7', 'n8', 'n9', 'n12'], 'n6', 500, True],
        ['12', G3, ['n7', 'n8', 'n9', 'n12'], 'n2', 500, False],
        ['13', G3, ['n7', 'n8', 'n9', 'n12'], 'n0', 5000, False],
    ])
    def test_base00(self, name, g, q_list, q, t, expected_result):
        self.assertEqual(is_candidate(g, q_list, q, t), expected_result)

    def test_None_Parameters(self):
        self.assertIsNone(is_candidate(None, ['n0'], 'n1', 1))
        self.assertIsNone(is_candidate(G1, None, 'n1', 1))
        self.assertIsNone(is_candidate(G1, ['n0'], None, 1))
        self.assertIsNone(is_candidate(G1, ['n0'], 'n1', None))

    def test_null_graph(self):
        self.assertIsNone(is_candidate(nx.Graph(), [0], 1, 1))

    def test_invalid_Q(self):
        self.assertIsNone(is_candidate(G1, ['n4', 'n5'], 'n0', 1))

    def test_invalid_q(self):
        self.assertIsNone(is_candidate(G1, ['n4', 'n2'], 'n5', 1))

    def test_q_in_Q(self):
        self.assertIsNone(is_candidate(G1, ['n4', 'n2'], 'n2', 1))

    def test_invalid_t(self):
        self.assertIsNone(is_candidate(G1, ['n4', 'n2'], 'n0', -1))


if __name__ == '__main__':
    unittest.main(verbosity=2)
