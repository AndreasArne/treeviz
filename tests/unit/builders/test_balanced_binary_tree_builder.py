"""
Tests treevizer builders
"""
import unittest
from unittest import mock
from tests.fixtures import tree_utils as utils
#pylint: disable=no-name-in-module,import-error, protected-access, attribute-defined-outside-init
from tests.fixtures.bst import BinarySearchTree as Bst
from tests.fixtures.bst import Node
from treevizer.builders.balanced_binary_tree import BalancedBinaryTree as BbtBuilder
from treevizer.exporters import png, dot

class TestBalanceBinaryTreeBuilder(unittest.TestCase):
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



    @mock.patch.object(BbtBuilder, '_add_vertex')
    @mock.patch.object(BbtBuilder, '_add_edge')
    @mock.patch.object(BbtBuilder, '_add_invis_node')
    def test_add_node_to_graph_one_node_has_both(self, invisMock, edgeMock, vertexMock):
        """
        Tests node having both children
        """
        root = Node(1, "None")
        n3 = Node(3.0, 0.0)
        n4 = Node("4. 4", "he j")
        root.left = n3
        n3.parent = root
        root.right = n4
        n4.parent = root
        bbt = BbtBuilder(root)

        vertex_calls = [
            mock.call(name=1, label=1),
            mock.call(name=3.0, label=3.0),
            mock.call(name="4. 4", label="4. 4"),
        ]
        vertexMock.assert_has_calls(vertex_calls)
        self.assertEqual(vertexMock.call_count, 3)

        invis_calls = [
            mock.call(3.0),
            mock.call(3.0),
            mock.call(3.0),
            mock.call(1),
            mock.call("4. 4"),
            mock.call("4. 4"),
            mock.call("4. 4"),
        ]
        invisMock.assert_has_calls(invis_calls)
        self.assertEqual(invisMock.call_count, 7)

        edge_calls = [
            mock.call(3.0, 1, "parent"),
            mock.call(1, 3.0, "left"),
            mock.call("4. 4", 1, "parent"),
            mock.call(1, "4. 4", "right"),
        ]
        edgeMock.assert_has_calls(edge_calls)
        self.assertEqual(edgeMock.call_count, 4)



    @mock.patch.object(BbtBuilder, '_add_vertex')
    @mock.patch.object(BbtBuilder, '_add_edge')
    @mock.patch.object(BbtBuilder, '_add_invis_node')
    def test_add_node_to_graph_one_node_has_right(self, invisMock, edgeMock, vertexMock):
        """
        Tests having right child only
        """
        root = Node(1, "None")
        n4 = Node("4. 4", "he j")
        root.right = n4
        n4.parent = root
        bbt = BbtBuilder(root)

        vertex_calls = [
            mock.call(name=1, label=1),
            mock.call(name="4. 4", label="4. 4"),
        ]
        vertexMock.assert_has_calls(vertex_calls)
        self.assertEqual(vertexMock.call_count, 2)

        invis_calls = [
            mock.call(1),
            mock.call(1),
            mock.call("4. 4"),
            mock.call("4. 4"),
            mock.call("4. 4"),
        ]
        invisMock.assert_has_calls(invis_calls)
        self.assertEqual(invisMock.call_count, 5)

        edge_calls = [
            mock.call("4. 4", 1, "parent"),
            mock.call(1, "4. 4", "right"),
        ]
        edgeMock.assert_has_calls(edge_calls)
        self.assertEqual(edgeMock.call_count, 2)



    @mock.patch.object(BbtBuilder, '_add_vertex')
    @mock.patch.object(BbtBuilder, '_add_edge')
    @mock.patch.object(BbtBuilder, '_add_invis_node')
    def test_add_node_to_graph_one_node_has_left(self, invisMock, edgeMock, vertexMock):
        """
        Tests having left child only
        """
        root = Node(1, "None")
        n2 = Node("2", None)
        root.left = n2
        n2.parent = root
        bbt = BbtBuilder(root)

        vertex_calls = [
            mock.call(name=1, label=1),
            mock.call(name="2", label="2"),
        ]
        vertexMock.assert_has_calls(vertex_calls)
        self.assertEqual(vertexMock.call_count, 2)

        invis_calls = [
            mock.call("2"),
            mock.call("2"),
            mock.call("2"),
            mock.call(1),
            mock.call(1),
        ]
        invisMock.assert_has_calls(invis_calls)
        self.assertEqual(invisMock.call_count, 5)

        edge_calls = [
            mock.call("2", 1, "parent"),
            mock.call(1, "2", "left"),
        ]
        edgeMock.assert_has_calls(edge_calls)
        self.assertEqual(edgeMock.call_count, 2)



    @mock.patch.object(BbtBuilder, '_add_vertex')
    @mock.patch.object(BbtBuilder, '_add_edge')
    @mock.patch.object(BbtBuilder, '_add_invis_node')
    def test_add_node_to_graph_one_node(self, invisMock, edgeMock, vertexMock):
        """
        Tests having no children
        """
        root = Node(1, "None")
        bbt = BbtBuilder(root)

        vertexMock.assert_called_once_with(name=1, label=1)
        invis_calls = [
            mock.call(1),
            mock.call(1),
            mock.call(1),
        ]
        invisMock.assert_has_calls(invis_calls)
        self.assertEqual(invisMock.call_count, 3)
        edgeMock.assert_not_called()



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
                with mock.patch('treevizer.builders.balanced_binary_tree.Edge') as edgeMock:
                    bbt = BbtBuilder("")
                    bbt.vertexes[src_key] = src_mock
                    bbt._add_invis_node(src_key)
    
            self.assertEqual(bbt.invis_counter, 1)
            edgeMock.assert_called_once_with(src_id, inv_id, style="invis", weight=5)
            self.assertEqual(len(bbt.edges), 1)
            self.assertEqual(len(bbt.vertexes), 2)



if __name__ == '__main__':
    unittest.main(verbosity=3)
