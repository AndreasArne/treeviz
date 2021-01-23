"""
Tests Treeviz builders
"""
import unittest
from unittest import mock
from fixtures import tree_utils as utils
#pylint: disable=no-name-in-module,import-error, protected-access, attribute-defined-outside-init
from fixtures.ll_node import Node
from treeviz.builders.linked_list import LinkedListGraph as LlBuilder
from treeviz.exporters import png, dot

class TestBuilders(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""
    
    # def test_full(self):
    #     root = Node(1, Node(4, Node(3, Node(1))))
    #     ll = LlBuilder(root)
    #     dot.to_dot(ll)
    #     png.create_png()



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
