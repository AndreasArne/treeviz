"""
Test with real data
"""
import unittest
import tempfile
from unittest import mock
from functools import update_wrapper
import treevizer
from tests.fixtures import tree_utils as utils
from tests.fixtures.bst import BinarySearchTree as Bst
from tests.fixtures.ll_node import Node

class TestIntegration(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""
    

    @mock.patch("treevizer.builders.vertex.id")
    def test_render_recursion(self, id_mock):
        """
        Test full run of recursion vizualize. Decorate 2 functions to check that decoration_order works.
        """
        @treevizer.recursion_viz
        def quicksort(items):
            if len(items) <= 1: 
                return items
            else:
                pivot = items[0]
                lesser = quicksort([x for x in items[1:] if x < pivot])
                greater = quicksort([x for x in items[1:] if x >= pivot])
                return lesser + [pivot] + greater
        
        @treevizer.recursion_viz
        def fib(n):
            if n <= 1:
                return n
            return fib(n=n - 1) + fib(n=n - 2)
        
        def side_effect(name):
            """
            If ID is not mocked it is bases on memory location, which we cant predict.
            Rename it, this way we catch that edges work correctly.
            Had a bug where a counter was use to ID vertexes and since this method before only return the argument, we didn't catch
            that outside the test, edges id's were the counter number and not ID.
            """
            return f"v{name}"
        id_mock.side_effect = side_effect

        fib(4)
        quicksort(list("helloworld"))

        self.assertEqual(len(treevizer.main.decorated_functions), 2)
        with tempfile.TemporaryDirectory(dir="./") as tmpdirname:
            treevizer.recursion_to_png("fib", tmpdirname+"/fibonacci.dot", tmpdirname+"/fibonacci.png")
            treevizer.recursion_to_png("quicksort",dot_path=tmpdirname+"/quicksort.dot", png_path=tmpdirname+"/quicksort.png")
            # breakpoint()
            with open(tmpdirname+"/fibonacci.dot", "rb") as test_dot:
                with open("tests/fixtures/integration_files/fibonacci.dot", "rb") as correct_dot:
                    self.assertEqual(test_dot.read(), correct_dot.read())

            with open(tmpdirname+"/quicksort.dot", "rb") as test_dot:
                with open("tests/fixtures/integration_files/quicksort.dot", "rb") as correct_dot:
                    self.assertEqual(test_dot.read(), correct_dot.read())



    @mock.patch("treevizer.builders.vertex.id")
    def test_to_png_bbt(self, id_mock):
        """
        Test full run of tree to png for bbt
        """
        def side_effect(name):
            """
            If ID is not mocked it is bases on memory location, which we cant predict.
            Rename it, this way we catch that edges work correctly.
            Had a bug where a counter was use to ID vertexes and since this method before only return the argument, we didn't catch
            that outside the test, edges id's were the counter number and not ID.
            """
            return f"v{name}"
        id_mock.side_effect = side_effect
    
        bst = Bst()
        utils.list_to_bst([10, 20, 0, 33, 2,  1, 15], bst)
    
        with tempfile.TemporaryDirectory(dir="./") as tmpdirname:
            treevizer.to_png(bst.root, "bbt", tmpdirname+"/tree file.dot", tmpdirname+"/tree.png")
            # breakpoint()
            with open(tmpdirname+"/tree file.dot", "rb") as test_dot:
                with open("tests/fixtures/integration_files/bst.dot", "rb") as correct_dot:
                    self.assertEqual(test_dot.read(), correct_dot.read())
    
    
    @mock.patch("treevizer.builders.vertex.id")
    def test_to_png_ll(self, id_mock):
        """
        Test full run of tree to png for ll
        """
        def side_effect(name):
            """
            If ID is not mocked it is bases on memory location, which we cant predict.
            Rename it, this way we catch that edges work correctly.
            Had a bug where a counter was use to ID vertexes and since this method before only return the argument, we didn't catch
            that outside the test, edges id's were the counter number and not ID.
            """
            return f"v{name}"
        id_mock.side_effect = side_effect
    
        ll = Node(10, Node(20, Node("0", Node(33, Node(2,  Node(1, Node("test")))))))
    
        with tempfile.TemporaryDirectory(dir="./") as tmpdirname:
            treevizer.to_png(ll, "ll", tmpdirname+"/tree.dot", tmpdirname+"/tree.png")
            # breakpoint()
            with open(tmpdirname+"/tree.dot", "rb") as test_dot:
                with open("tests/fixtures/integration_files/ll.dot", "rb") as correct_dot:
                    self.assertEqual(test_dot.read(), correct_dot.read())
