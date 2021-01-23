"""
Tests Treeviz builders
"""
import unittest
from unittest import mock
from fixtures import tree_utils as utils
#pylint: disable=no-name-in-module,import-error, protected-access, attribute-defined-outside-init
from fixtures.bst import BinarySearchTree as Bst
from fixtures.bst import Node
from treeviz.builders.balanced_binary_tree import BalancedBinaryTreeGraph as BbtBuilder
from treeviz.exporters import png, dot

class TestBuilders(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    # def test_bbt_to_png(self):
    #     """
    #     Method for creating a picture of tree,
    #     Nothing is tested. 
    #     """
    #     nr_tree_nodes = 11
    #     self._setUp(nr_tree_nodes)
    #     # Adds a ghost node
    #     self.bst.root.left.parent = Node(99,99)
    # 
    #     bbt = BbtBuilder(self.bst.root)
    #     dot.to_dot(bbt)
    #     png.create_png()



    def test_graph_type(self):
        self.assertEqual(BbtBuilder.graph_type(), "digraph")



    def test_create_bbt_on_empty_tree(self):
        """
        Try create a balance binary tree with None sent as root
        """
        with self.assertRaises(ValueError):
            _ = BbtBuilder(None)



    def test_add_invis_node_mock(self):
        """
        add an invis node
        """
        inv_key = "i1"
        inv_id = 1
        src_id = 0
        src_key = "1"
        src_mock = mock.MagicMock()
        src_mock.id = src_id

        def add_vertex(self_, name, label, style):
            self.assertEqual(name, inv_key)
            self.assertEqual(label, inv_key)
            self.assertEqual(style, "invis")

            inv_vertex_mock = mock.MagicMock()
            inv_vertex_mock.id = inv_id
            self_.vertexes[inv_key] = inv_vertex_mock

        with mock.patch.object(BbtBuilder, "_add_node_to_graph", lambda x, y: None): # Match number of args for init and return None
            with mock.patch.object(BbtBuilder, '_add_vertex', autospec=True, side_effect=add_vertex):
                with mock.patch('treeviz.builders.balanced_binary_tree.Edge') as edgeMock:
                    bbt = BbtBuilder("")
                    bbt.vertexes[src_key] = src_mock
                    bbt._add_invis_node(src_key)
    
            self.assertEqual(bbt.invis_counter, 1)
            edgeMock.assert_called_once_with(src_id, inv_id, style="invis", weight=5)
            self.assertEqual(len(bbt.edges), 1)
            self.assertEqual(len(bbt.vertexes), 2)



if __name__ == '__main__':
    unittest.main(verbosity=3)
