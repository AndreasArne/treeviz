"""
Test with real data
"""
import unittest
import tempfile
from unittest import mock
import treevizer
from tests.fixtures import tree_utils as utils
from tests.fixtures.bst import BinarySearchTree as Bst
from tests.fixtures.ll_node import Node

class TestIntegration(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""
    
    
    @mock.patch("treevizer.builders.vertex.id")
    def test_tree_to_png_bbt(self, id_mock):
        """
        Test full run of tree to png for bbt
        """
        def side_effect(name):
            return name
        id_mock.side_effect = side_effect

        bst = Bst()
        utils.list_to_bst([10, 20, 0, 33, 2,  1, 15], bst)
        
        with tempfile.TemporaryDirectory(dir="./") as tmpdirname:
            treevizer.tree_to_png(bst.root, "bbt", tmpdirname+"/tree.dot", tmpdirname+"/tree.png")
            with open(tmpdirname+"/tree.dot", "rb") as test_dot:
                with open("tests/fixtures/integration_files/bst.dot", "rb") as correct_dot:
                    self.assertEqual(test_dot.read(), correct_dot.read())


    @mock.patch("treevizer.builders.vertex.id")
    def test_tree_to_png_ll(self, id_mock):
        """
        Test full run of tree to png for ll
        """
        def side_effect(name):
            return name
        id_mock.side_effect = side_effect

        ll = Node(10, Node(20, Node("0", Node(33, Node(2,  Node(1, Node("test")))))))
        
        with tempfile.TemporaryDirectory(dir="./") as tmpdirname:
            treevizer.tree_to_png(ll, "ll", tmpdirname+"/tree.dot", tmpdirname+"/tree.png")
            with open(tmpdirname+"/tree.dot", "rb") as test_dot:
                with open("tests/fixtures/integration_files/ll.dot", "rb") as correct_dot:
                    self.assertEqual(test_dot.read(), correct_dot.read())
