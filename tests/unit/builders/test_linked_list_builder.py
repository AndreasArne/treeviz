"""
Tests treevizer builders
"""
import unittest
from unittest import mock
from tests.fixtures import tree_utils as utils
#pylint: disable=no-name-in-module,import-error, protected-access, attribute-defined-outside-init
from tests.fixtures.ll_node import Node
from treevizer.builders.linked_list import LinkedListGraph as LlBuilder
from treevizer.exporters import png, dot

class TestBuilders(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""
    
    # def test_full(self):
    #     root = Node(1, Node(4, Node(3, Node(1))))
    #     ll = LlBuilder(root)
    #     dot.to_dot(ll)
    #     png.create_png()

    def test_add_node_to_graph_tree_nodes(self):
        """
        Tests entering while loop more than once
        """
        with mock.patch.object(LlBuilder, '_add_vertex') as addVertexMock:
            with mock.patch.object(LlBuilder, '_add_edge') as addEdgeMock:
                self.llb = LlBuilder(Node("1",Node(2, Node("te st"))))

                vertex_calls = [
                    mock.call(name=0, label='i=0\nv=1'),
                    mock.call(name=1, label='i=1\nv=2'),
                    mock.call(name=2, label='i=2\nv=te st'),
                ]
                addVertexMock.assert_has_calls(vertex_calls)
                self.assertEqual(addVertexMock.call_count, 3)
                
                edge_calls = [
                    mock.call(0, 1),
                    mock.call(1, 2),
                ]
                addEdgeMock.assert_has_calls(edge_calls)
                self.assertEqual(addEdgeMock.call_count, 2)



    def test_add_node_to_graph_two_nodes(self):
        """
        Tests entering while loop once
        """
        with mock.patch.object(LlBuilder, '_add_vertex') as addVertexMock:
            with mock.patch.object(LlBuilder, '_add_edge') as addEdgeMock:
                self.llb = LlBuilder(Node("1",Node(2)))

                vertex_calls = [
                    mock.call(name=0, label='i=0\nv=1'),
                    mock.call(name=1, label='i=1\nv=2'),
                ]
                addVertexMock.assert_has_calls(vertex_calls)
                self.assertEqual(addVertexMock.call_count, 2)
                addEdgeMock.assert_called_once_with(0, 1)



    def test_add_node_to_graph_one_node(self):
        """
        Test not entering while loop
        """
        with mock.patch.object(LlBuilder, '_add_vertex') as addMock:
            self.llb = LlBuilder(Node(1))
            addMock.assert_called_once_with(name=0, label="i=0\nv=1")



    def test_create_linked_list_builder_with_none(self):
        """
        Try create a Linked List builder with None sent as root
        """
        with self.assertRaises(ValueError):
            _ = LlBuilder(None)



    def test_graph_type(self):
        self.assertEqual(LlBuilder.graph_type(), "digraph")



if __name__ == '__main__':
    unittest.main(verbosity=3)
