"""
Tests Treeviz builders
"""
import unittest
from unittest import mock
import tree_utils as utils
#pylint: disable=no-name-in-module,import-error, protected-access, attribute-defined-outside-init
from bst import BinarySearchTree as Bst
from treeviz.builders.balanced_binary_tree import BalancedBinaryTreeGraph as BbtBuilder
from treeviz.exporters import png, dot

class TestBuilders(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def _setUp(self, size):
        """ Custom setup to control size of tree use for tests """
        self.bst = Bst()
        self.insert_seq = utils.random_seq(size)
        utils.list_to_bst(self.insert_seq, self.bst)

    def tearDown(self):
        """ teardown test """
        self.bst = None
        self.insert_seq = None

    def test_create_bbt_sucessfully(self):
        """
        Try create a balance binary tree
        from a binary search tree.
        Bad test, too big! But works wondefully
        """
        nr_tree_nodes = 11
        self._setUp(nr_tree_nodes)
        bbt = BbtBuilder(self.bst.root)
        NR_CHILD_NODES_P_NODE = 3
        graph_number_nodes = nr_tree_nodes * NR_CHILD_NODES_P_NODE + 1 # 1 for root node

        # uncomment to ses files
        dot.to_dot(bbt)
        png.create_png()
        # exit()

        # Check correct number of nodes in tree
        self.assertEqual(len(bbt.vertexes), graph_number_nodes)

        # Check correct visible nodes
        graph_nodes = bbt.vertexes
        for i in range(nr_tree_nodes):
            self.assertIn(str(i), graph_nodes)
        # self.assertEqual(bbt.graph.vs["style"].count("filled"), nr_tree_nodes)

        # Check correct invis nodes to balance tree
        nr_invis_nodes = graph_number_nodes - nr_tree_nodes
        for i in range(1, nr_invis_nodes):
            self.assertIn("i"+str(i), graph_nodes)
        # self.assertEqual(bbt.graph.vs["style"].count("invis"), nr_invis_nodes)

        # one_less_reference_for_root = 0
        # for node in utils.get_nodes_neighbors(self.bst.root):
        #     # check arrows to node
        #     in_nodes = [n["name"] for n in bbt.graph.vs.find(name=node[0]).predecessors()]
        #     node_references = node[1:]
        #     for n in in_nodes:
        #         if not n.startswith("i"):
        #             self.assertIn(n, node_references)
        
        #     # check arrows from node
        #     out_nodes = [n["name"] for n in bbt.graph.vs.find(name=node[0]).successors()]
        #     expected_nr_invis_nodes = one_less_reference_for_root + node_references.count(None)
        #     invis_node_counter = 0
        #     for n in out_nodes:
        #         if n.startswith("i"):
        #             invis_node_counter += 1
        #         else:
        #             self.assertIn(n, node_references)
        #     self.assertEqual(expected_nr_invis_nodes, invis_node_counter)
        #     one_less_reference_for_root = 1



    def test_create_bbt_on_empty_tree(self):
        """
        Try create a balance binary tree with None sent as root
        """
        with self.assertRaises(ValueError):
            _ = BbtBuilder(None)



    def test_add_edge_to_nonexisting_node(self):
        """
        Try to add edge between node that does not exist
        and check that it is added.
        """
        key = "1"
        other_key = "2"
        bbt_mock = mock.MagicMock()
        vertex_mock = mock.MagicMock()
        vertex_mock.id = 0
        bbt_mock.vertexes = {"1":vertex_mock}
        BbtBuilder._add_edge(bbt_mock, key, other_key)
        
        bbt_mock._add_vertex.assert_called_once_with(
            name=other_key,
            label=other_key,
            style="filled"
        )



    def test_add_invis_node_mock(self):
        """
        Try to add an invis node
        Example of using mock to lose dependency on Igraph
        """
        key = "1"
        inv_key = "i4"
        bbt_mock = mock.MagicMock()
        bbt_mock.invis_counter = 3
        with mock.patch('treeviz.builders.balanced_binary_tree.Edge') as EdgeMock:
            BbtBuilder._add_invis_node(bbt_mock, key)

            self.assertEqual(bbt_mock.invis_counter, 4)
            bbt_mock._add_vertex.assert_called_once_with(
                inv_key,
                label=inv_key,
                style="invis"
            )
            EdgeMock.assert_called_once()



if __name__ == '__main__':
    unittest.main(verbosity=3)
