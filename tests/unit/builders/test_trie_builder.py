"""
Tests treevizer builders
"""
import unittest
from unittest import mock
from tests.fixtures import tree_utils as utils
from tests.fixtures.trie import Node
from treevizer.builders.trie import Trie

class TestTrieBuilder(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def test_add_node_stop(self):
        """
        Test that special vertex is created for stop node.
        """
        n = Node("a")
        n["n"] = Node("n")
        n["n"].stop = True

        vertex_calls = [
            mock.call(name="a", label="a"),
            mock.call(name="an", label="n", html_xlabel='<FONT COLOR="grey25" POINT-SIZE="12">an</FONT>', fillcolor="forestgreen", color="black")
        ]

        with mock.patch.object(Trie, '_add_vertex') as vertexMock:
            with mock.patch.object(Trie, '_add_edge') as edgeMock:
                trie = Trie(n)
                vertexMock.assert_has_calls(vertex_calls)
                edgeMock.assert_called_once_with("a", "an")



    def test_add_node_reraise_exception(self):
        """
        Test exception is re raised when type error does not contain "not iterale"
        """
        def raiseTypeError(children, word):
            raise TypeError()

        n = Node("a")
        n.children = "test"
        with mock.patch.object(Trie, '_add_vertex') as addMock:
            with mock.patch.object(Trie, 'add_children') as childrenMock:
                childrenMock.side_effect = raiseTypeError
                with self.assertRaises(TypeError) as err:
                    trie = Trie(n)
                    self.assertTrue(
                        "Use list, dict or other iterable datastructure." not in str(err)
                    )
                    addMock.assert_called_once_with(name="a", label="a")



    def test_add_node_children_type_exception(self):
        """
        Test exception is raised when children has wrong type
        """
        n = Node("a")
        n.children = 2
        with mock.patch.object(Trie, '_add_vertex') as addMock:
            with self.assertRaises(TypeError):
                trie = Trie(n)
            addMock.assert_called_once_with(name="a", label="a")



    def test_create_xlabel(self):
        """
        Test xlabel has html elements
        """
        label = Trie.create_xlabel("test ing")
        self.assertEqual(
            label,
            '<FONT COLOR="grey25" POINT-SIZE="12">test ing</FONT>'
        )



    def test_create_trie_builder_with_none(self):
        """
        Try create a Trie builder with None sent as root
        """
        with self.assertRaises(ValueError):
            _ = Trie(None)



    def test_graph_type(self):
        self.assertEqual(Trie.graph_type(), "digraph")



if __name__ == '__main__':
    unittest.main(verbosity=3)
