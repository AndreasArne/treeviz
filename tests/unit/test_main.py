"""
Test config reader
"""
import unittest
from unittest import mock
from treevizer import main

class TestMain(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def tearDown(self):
        main.decorated_functions = {}


    def test_contant_variables(self):
        """
        Assert constant variables are as expected
        """
        self.assertEqual(main.AVAILABLE_TREES, "balanced binary tree (bbt), linked list (ll)")



    @mock.patch("treevizer.main.Recursion")
    def test_recursion_viz(self, recursion_mock):
        """
        Test that to_dot is called correctly for recursion
        and create_png is called.
        """
        @main.recursion_viz
        def test_func():
            """Wrapped works"""
            pass

        self.assertEqual(test_func.__doc__, "Wrapped works")
        self.assertEqual(test_func.__name__, "test_func")
        test_func()
        recursion_mock.assert_called_once()
        self.assertEqual(len(main.decorated_functions), 1)



    def test_recursion_to_png_exception(self):
        """
        Test that to_dot is called correctly for recursion
        and create_png is called.
        """
        recursion_mock = mock.MagicMock()
        main.decorated_functions["nane"] = recursion_mock
        with self.assertRaises(ValueError):
            main.recursion_to_png("missing name", "rec.dot", "rec.png")



    @mock.patch("treevizer.main.dot")
    @mock.patch("treevizer.main.png")
    def test_recursion_to_png(self, mock_png, mock_dot):
        """
        Test that to_dot is called correctly for recursion
        and create_png is called.
        """
        recursion_mock = mock.MagicMock()
        main.decorated_functions["name"] = recursion_mock
        main.recursion_to_png("name", dot_path="rec.dot", png_path="rec.png")
        mock_dot.to_dot.assert_called_once_with(recursion_mock, "rec.dot")
        mock_png.create_png.assert_called_once_with("rec.dot", "rec.png")




    def test_to_dot_missing_type(self):
        """
        Test that error is raised when its wrong type
        """
        node_mock = mock.MagicMock()
        with self.assertRaises(ValueError):
            main.to_dot(node_mock, "trie")



    def test_to_dot_root_is_none(self):
        """
        Test that error is raised when root is None
        """
        with self.assertRaises(ValueError):
            main.to_dot(None, "ll")



    @mock.patch("treevizer.main.png")
    def test_dot_to_png(self, mock_png):
        """
        Test that create_png is called correctly
        """
        main.dot_to_png("ll.dot", "ll.png")
        mock_png.create_png.assert_called_once_with("ll.dot", "ll.png")



    @mock.patch("treevizer.main.dot")
    @mock.patch("treevizer.main.ll")
    @mock.patch("treevizer.main.png")
    def test_to_png_ll(self, mock_png, mock_ll, mock_dot):
        """
        Test that to_dot is called correctly for ll
        and create_png is called.
        """
        node_mock = mock.MagicMock()
        main.to_png(node_mock, "ll", "ll.dot")
        mock_ll.assert_called_once_with(node_mock)
        mock_dot.to_dot.assert_called_once_with(mock_ll(), "ll.dot")
        mock_png.create_png.assert_called_once_with("ll.dot", "tree.png")



    @mock.patch("treevizer.main.dot")
    @mock.patch("treevizer.main.ll")
    def test_to_dot_ll(self, mock_ll, mock_dot):
        """
        Test that to_dot is called correctly for ll
        """
        node_mock = mock.MagicMock()
        main.to_dot(node_mock, "ll", "ll.dot")
        mock_ll.assert_called_once_with(node_mock)
        mock_dot.to_dot.assert_called_once_with(mock_ll(), "ll.dot")



    @mock.patch("treevizer.main.dot")
    @mock.patch("treevizer.main.bbt")
    def test_to_dot_bbt(self, mock_bbt, mock_dot):
        """
        Test that to_dot is called correctly for bbt
        """
        node_mock = mock.MagicMock()
        main.to_dot(node_mock, "bbt", "bbt.dot")
        mock_bbt.assert_called_once_with(node_mock)
        mock_dot.to_dot.assert_called_once_with(mock_bbt(), "bbt.dot")
