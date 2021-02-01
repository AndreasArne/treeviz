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
    
    
    def test_tree_to_png_bbt(self):
        """
        Test full run of tree to png for bbt
        """
        bst = Bst()
        utils.list_to_bst([10, 20, 0, 33, 2,  1, 15], bst)
        
        with tempfile.TemporaryDirectory(dir="./") as tmpdirname:
            treevizer.tree_to_png(bst.root, "bbt", tmpdirname+"/tree.dot", tmpdirname+"/tree.png")
            with open(tmpdirname+"/tree.png", "rb") as test_png:
                with open("tests/fixtures/integration_files/bst.png", "rb") as correct_png:
                    self.assertEqual(test_png.read(), correct_png.read())



    def test_tree_to_png_ll(self):
        """
        Test full run of tree to png for ll
        """
        ll = Node(10, Node(20, Node("0", Node(33, Node(2,  Node(1, Node("test")))))))
        
        with tempfile.TemporaryDirectory(dir="./") as tmpdirname:
            treevizer.tree_to_png(ll, "ll", tmpdirname+"/tree.dot", tmpdirname+"/tree.png")
            with open(tmpdirname+"/tree.png", "rb") as test_png:
                with open("tests/fixtures/integration_files/ll.png", "rb") as correct_png:
                    self.assertEqual(test_png.read(), correct_png.read())
