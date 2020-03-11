"""
Tests Treeviz builders
"""
import unittest
from unittest import mock
import tree_utils as utils
#pylint: disable=no-name-in-module,import-error, protected-access, attribute-defined-outside-init
from bst import BinarySearchTree as Bst
import treeviz
# from treeviz.exporters import png, dot

class TestBuilders(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def _setUp(self, size):
        """ Custom setup to control size of tree use for tests """
        self.bst = Bst()
        self.insert_seq = utils.random_seq(size)
        utils.list_to_bst(self.insert_seq, self.bst)

    def tearDown(self):
        """ teardown test """
        self.bst = None
        self.insert_seq = None


    def test_tree_to_png(self):
        size = 10
        self._setUp(size)
        # treeviz.tree_to_png()

if __name__ == '__main__':
    unittest.main(verbosity=3)
