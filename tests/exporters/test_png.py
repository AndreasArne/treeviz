"""
Tests Treeviz png exporter
"""
import unittest
from unittest import mock
#pylint: disable=no-name-in-module,import-error, protected-access, attribute-defined-outside-init
from treeviz.exporters import png

class TestPngExporter(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    @mock.patch("treeviz.exporters.png.os.system")
    def test_create_png(self, os_mock):
        png.create_png()
        



if __name__ == '__main__':
    unittest.main(verbosity=3)
