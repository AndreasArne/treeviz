"""
Tests Graph builders
"""
import unittest
from unittest import mock
from tests.fixtures import tree_utils as utils
#pylint: disable=no-name-in-module,import-error, protected-access, attribute-defined-outside-init
from treeviz.builders.base_graph import Graph
from tests.fixtures.ll_node import Node


class TestGraphBuilder(unittest.TestCase):

    def setUp(self):
        with mock.patch.object(Graph, "_add_node_to_graph", lambda x, y: None): # Match number of args for init and return None
            self.g = Graph(mock.MagicMock())



    def test_graph_type(self):
        self.assertEqual(Graph.graph_type(), "digraph")
        self.assertEqual(self.g.graph_type(), "digraph")




    def test_abstract_method_add_nodes(self):
        """
        Test that NotImplementedError is raised when creating Object
        """
        with self.assertRaises(NotImplementedError) as e:
            _ = Graph(mock.MagicMock())



    @mock.patch('builtins.print')
    def test_add_edge_when_dest_vertex_missing(self, mock_print):
        """
        add edge when the destination vertex is missing.
        """
        src_id = 0
        dest_id = 1
        def side_effect(self_, name, label, color):
            self.assertEqual(color, "red")
            self.assertEqual(name, 2)
            self.assertEqual(label, 2)

            dest_mock = mock.MagicMock()
            dest_mock.id = dest_id
            self_.vertexes[2] = dest_mock

        with mock.patch.object(Graph, "_add_node_to_graph", lambda x, y: None): # Match number of args for init and return None
            src_mock = mock.MagicMock()
            src_mock.id = src_id
            self.g.vertexes[1] = src_mock
            
            with mock.patch.object(Graph, '_add_vertex', autospec=True, side_effect=side_effect):
                with mock.patch('treeviz.builders.base_graph.Edge') as edgeMock:
                    self.g._add_edge(1, 2, "parent")

                    edgeMock.assert_called_once_with(src_id, dest_id, label="parent", color="red")
        mock_print.assert_called_once()
        self.assertEqual(len(self.g.vertexes), 2)
        self.assertEqual(len(self.g.edges), 1)



    def test_add_edge(self,):
        """
        add edge when all vertexes exist.
        """
        src_id = 0
        dest_id = 1

        src_mock = mock.MagicMock()
        src_mock.id = src_id
        dest_mock = mock.MagicMock()
        dest_mock.id = dest_id
        self.g.vertexes[1] = src_mock
        self.g.vertexes[2] = dest_mock

        with mock.patch('treeviz.builders.base_graph.Edge') as edgeMock:
            self.g._add_edge(1, 2)
            
            edgeMock.assert_called_once_with(src_id, dest_id)
        self.assertEqual(len(self.g.vertexes), 2)
        self.assertEqual(len(self.g.edges), 1)



    def test_add_edge_raise_exception_when_src_vertex_missing(self):
        """
        add edge when the source vertex is missing
        """
        with self.assertRaises(ValueError):
            self.g.vertexes[1] = Node(1)
            self.g._add_edge(2, 1, "not relevant")



    def test_add_vertex_no_kwargs(self):
        """
        add vertex correctly, no kwargs
        """
        with mock.patch('treeviz.builders.base_graph.Vertex') as vertexMock:
            self.g._add_vertex(2)
            vertexMock.assert_called_once_with(2)
            
        self.assertEqual(len(self.g.vertexes), 1)



    def test_add_vertex_kwargs(self):
        """
        add vertex correctly with kwargs
        """
        with mock.patch('treeviz.builders.base_graph.Vertex') as vertexMock:
            self.g._add_vertex(2, style="filled", color="red")

            vertexMock.assert_called_once_with(2, style="filled", color="red")
        self.assertEqual(len(self.g.vertexes), 1)



    def test_add_vertex_already_exist(self):
        """
        Testa that error is raised when a Vertex already exist.
        """
        self.g.vertexes[1] = Node(1)
        with self.assertRaises(KeyError):
            self.g._add_vertex(1)



    def test_create_graph_with_none(self):
        """
        Try create a Graph tree with None sent as root
        """
        with self.assertRaises(ValueError):
            _ = Graph(None)
