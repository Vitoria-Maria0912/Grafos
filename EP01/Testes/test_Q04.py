import unittest
import networkx as nx
from EP01.src.Q04 import best_route
from parameterized import parameterized

# Author: Patrícia Duarte de Lima Machado

# Test Data
F1 = nx.Graph()
F1.add_nodes_from([(0, {'depth': 0, 'full': False}),
                   (1, {'depth': 30, 'full': False}),
                   (2, {'depth': 15, 'full': False}),
                   (3, {'depth': 0, 'full': False}),
                   (4, {'depth': 100, 'full': False}),
                   (5, {'depth': 6, 'full': False}),
                   (6, {'depth': 24, 'full': False}),
                   (7, {'depth': 35, 'full': False}),
                   (8, {'depth': 48, 'full': False})])
F1.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 8), (2, 7), (2, 6), (2, 4), (3, 5), (6, 7), (7, 8), (5, 1)])
F2 = nx.Graph()
F2.add_nodes_from([(0, {'depth': 0, 'full': False}),
                   (1, {'depth': 30, 'full': True}),
                   (2, {'depth': 15, 'full': True}),
                   (3, {'depth': 0, 'full': True}),
                   (4, {'depth': 100, 'full': True}),
                   (5, {'depth': 6, 'full': True}),
                   (6, {'depth': 24, 'full': True}),
                   (7, {'depth': 35, 'full': True}),
                   (8, {'depth': 48, 'full': True})])
F2.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 8), (2, 7), (2, 6), (2, 4), (3, 5), (6, 7), (7, 8), (5, 1)])
F3 = nx.Graph()
F3.add_nodes_from([(0, {'depth': 0, 'full': True}),
                   (1, {'depth': 30, 'full': False}),
                   (2, {'depth': 15, 'full': False}),
                   (3, {'depth': 0, 'full': False}),
                   (4, {'depth': 100, 'full': False}),
                   (5, {'depth': 6, 'full': False}),
                   (6, {'depth': 24, 'full': False}),
                   (7, {'depth': 35, 'full': False}),
                   (8, {'depth': 48, 'full': False})])
F3.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 8), (2, 7), (2, 6), (2, 4), (3, 5), (6, 7), (7, 8), (5, 1)])
F4 = nx.Graph()
F4.add_nodes_from([(0, {'depth': 0, 'full': False}),
                   (1, {'depth': 30, 'full': False}),
                   (2, {'depth': 15, 'full': False}),
                   (3, {'depth': 20, 'full': False}),
                   (4, {'depth': 100, 'full': False}),
                   (5, {'depth': 6, 'full': True}),
                   (6, {'depth': 24, 'full': True}),
                   (7, {'depth': 35, 'full': True}),
                   (8, {'depth': 48, 'full': False})])
F4.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 8), (2, 7), (2, 6), (2, 4), (3, 5), (6, 7), (7, 8), (5, 1)])
F5 = nx.Graph()
F5.add_nodes_from([(0, {'depth': 10, 'full': False}),
                   (1, {'depth': 30, 'full': False}),
                   (2, {'depth': 15, 'full': True}),
                   (3, {'depth': 0, 'full': False}),
                   (4, {'depth': 100, 'full': False}),
                   (5, {'depth': 6, 'full': True}),
                   (6, {'depth': 24, 'full': False}),
                   (7, {'depth': 35, 'full': True}),
                   (8, {'depth': 48, 'full': False})])
F5.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 8), (2, 7), (2, 6), (2, 4), (3, 5), (6, 7), (7, 8), (5, 1)])
F6 = nx.house_graph()
F6.nodes[0]['depth'], F6.nodes[0]['full'] = 0, False
F6.nodes[1]['depth'], F6.nodes[1]['full'] = 0, False
F6.nodes[2]['depth'], F6.nodes[2]['full'] = 0, False
F6.nodes[3]['depth'], F6.nodes[3]['full'] = 0, False
F6.nodes[4]['depth'], F6.nodes[4]['full'] = 0, False
F7 = nx.house_graph()
F7.nodes[0]['depth'], F7.nodes[0]['full'] = 0, False
F7.nodes[1]['depth'], F7.nodes[1]['full'] = 10, False
F7.nodes[2]['depth'], F7.nodes[2]['full'] = 50, False
F7.nodes[3]['depth'], F7.nodes[3]['full'] = 30, False
F7.nodes[4]['depth'], F7.nodes[4]['full'] = 40, False
F8 = nx.house_graph()
F8.nodes[0]['depth'], F8.nodes[0]['full'] = 0, False
F8.nodes[1]['depth'], F8.nodes[1]['full'] = 10, False
F8.nodes[2]['depth'], F8.nodes[2]['full'] = 50, False
F8.nodes[3]['depth'], F8.nodes[3]['full'] = 30, True
F8.nodes[4]['depth'], F8.nodes[4]['full'] = 40, False
F9 = nx.Graph()
F9.add_nodes_from([(0, {'depth': 0, 'full': False})])


class TestBestRoute(unittest.TestCase):

    @parameterized.expand([
        # name, g, node, expected_result
        ["F1", F1, 0, [0, 2, 6, 7, 8]],
        ["F2", F2, 0, [0]],
        ["F3", F3, 0, []],
        ["F4", F4, 0, [0, 2, 4]],
        ["F5", F5, 3, [3, 1, 8]],
        ["F6", F6, 3, [3]],
        ["F7", F7, 0, [0, 1, 3, 4, 2]],
        ["F8", F8, 0, [0, 1]],
        ["F9", F9, 0, [0]]
    ])
    def test_base00(self, name, g, node, expected_result):
        result = best_route(g, node)
        self.assertEqual(result, expected_result)

    def test_null_graph(self):
        self.assertTrue(best_route(nx.Graph(), 0) is None)

    def test_None_graph(self):
        self.assertTrue(best_route(None, 0) is None)

    def test_None_Node(self):
        self.assertTrue(best_route(F1, None) is None)

    def test_invalid_Node(self):
        self.assertTrue(best_route(F1, 20) is None)

    def test_invalid_initial_depth(self):
        self.assertTrue(best_route(F1, 1) is None)

    def test_no_node_full_attribute(self):
        g = nx.Graph()
        g.add_node(1, depth=20)
        self.assertTrue(best_route(g, 1) is None)

    def test_no_node_depth_attribute(self):
        g = nx.Graph()
        g.add_node(1, full=False)
        self.assertTrue(best_route(g, 1) is None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
