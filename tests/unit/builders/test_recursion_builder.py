"""
Tests treevizer builders
"""
import unittest
from unittest import mock
from functools import update_wrapper
from treevizer.builders.recursion import Recursion
from treevizer.exporters import png, dot

class TestRecursionBuilder(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def test_create_fn_call_str_args_kwargs(self):
        """
        Build call string with args and kwargs
        """
        def test_func():
            pass
        decorator = update_wrapper(Recursion(test_func), test_func)
        self.assertEqual(
            decorator._create_fn_call_str([1, "2"], {"kwarg":1, "kwarg2":"2"}),
            "test_func(1, &#x27;2&#x27;, kwarg=1, kwarg2=&#x27;2&#x27;)"
        )



    def test_create_fn_call_str_args(self):
        """
        Build call string with only args
        """
        def test_func():
            pass
        decorator = update_wrapper(Recursion(test_func), test_func)
        self.assertEqual(
            decorator._create_fn_call_str([1, "2"], {}),
            "test_func(1, &#x27;2&#x27;)"
        )


    def test_create_fn_call_str_kwargs(self):
        """
        Build call string with only kwargs
        """
        def test_func():
            pass
        decorator = update_wrapper(Recursion(test_func), test_func)
        self.assertEqual(
            decorator._create_fn_call_str([], {"kwarg":[1], "kwarg2":"2"}),
            "test_func(kwarg=[1], kwarg2=&#x27;2&#x27;)"
        )


    def test_create_fn_call_str_no_args_kwargs(self):
        """
        Build call string with no args or kwargs
        """
        def test_func():
            pass
        decorator = update_wrapper(Recursion(test_func), test_func)
        self.assertEqual(
            decorator._create_fn_call_str([], {}),
            "test_func()"
        )
    


    def test_graph_type(self):
        self.assertEqual(Recursion.graph_type(), "digraph")



if __name__ == '__main__':
    unittest.main(verbosity=3)
